from __future__ import annotations
import logging
import threading
from concurrent.futures import ThreadPoolExecutor
from os import listdir, chmod
from time import time, perf_counter

import psycopg2
from psycopg2 import connection
from psycopg2.pool import ThreadedConnectionPool

import leanit_mweb
from leanit_mweb.thread import AdvancedThreadPoolExecutor

logger = logging.getLogger(__name__)

from typing import TYPE_CHECKING, Iterable, Dict, Union

if TYPE_CHECKING:
    pass

local = threading.local()

def _initialize():
    thread_name = threading.current_thread().name
    logger.info(f"[{thread_name}] Initializing YugabyteDB connection pool")

    kwargs = dict(
        dbname=leanit_mweb.config['db']['dbname'],
        host=leanit_mweb.config['db']['host'],
        port=leanit_mweb.config['db']['port'],
        user=leanit_mweb.config['db']['user'],
        password=leanit_mweb.config['db']['password'],
        load_balance='true',
    )
    if 'sslmode' in leanit_mweb.config['db']:
        kwargs['sslmode'] = leanit_mweb.config['db']['sslmode']
    if 'sslcert' in leanit_mweb.config['db']:
        sslcert = leanit_mweb.config['db']['sslcert']
        if"BEGIN CERTIFICATE" in sslcert:
            # assume it's a certificate
            sslcert_path = f"/tmp/{kwargs['dbname']}-{thread_name}-sslcert.crt"
            with open(sslcert_path, "w") as f:
                f.write(sslcert.strip())
        else:
            # assume it's a file path
            sslcert_path = sslcert

        kwargs['sslcert'] = sslcert_path
    if 'sslkey' in leanit_mweb.config['db']:
        sslkey = leanit_mweb.config['db']['sslkey']
        if "PRIVATE KEY" in sslkey:
            # assume it's a private key
            sslkey_path = f"/tmp/{kwargs['dbname']}-{thread_name}-sslkey.key"
            with open(sslkey_path, "w") as f:
                chmod(sslkey_path, 0o600)
                f.write(sslkey.strip())
        else:
            # assume it's a file path
            sslkey_path = sslkey

        kwargs['sslkey'] = sslkey_path
    if 'sslrootcert' in leanit_mweb.config['db']:
        sslrootcert = leanit_mweb.config['db']['sslrootcert']
        if "BEGIN CERTIFICATE" in sslrootcert:
            # assume it's a certificate
            sslrootcert_path = f"/tmp/{kwargs['dbname']}-{thread_name}-sslrootcert.crt"
            with open(sslrootcert_path, "w") as f:
                f.write(sslrootcert.strip())

        else:
            # assume it's a file path
            sslrootcert_path = sslrootcert

        kwargs['sslrootcert'] = sslrootcert_path

    try:
        local.conn = psycopg2.connect(**kwargs)
    except Exception as e:
        logger.error(f"[{threading.current_thread().name}] Error initializing YugabyteDB connection pool: {e}")
        raise e

class YugabytedbThreadPool(AdvancedThreadPoolExecutor):
    """
    Usage:
        db = YugabytedbThreadPool(
            min_workers=3,
            max_workers=3
        )

        # in async event loop
        result = await asyncio.get_event_loop().run_in_executor(db, db.submit_sql, "SELECT 1")
    """
    def __init__(self, *args, **kwargs):
        kwargs['initializer'] = _initialize
        super().__init__(*args, **kwargs)

    def execute(self, sql: str, vars: Union[Dict, Iterable]=None):
        """
        This function is executed in the main thread (e.g. in async event loop)

        :param sql: might contain %s placeholders (vars=Iterable) or %(name)s placeholders (vars=Dict)
        :param vars: Iterable or Dict
        :return:
        """
        f = self.submit(self.submit_sql, sql, vars)
        return f.result()

    def submit_sql(self, sql: str, vars: Union[Dict, Iterable]=None):
        """
        This function is executed in a thread

        :param sql: might contain %s placeholders (vars=Iterable) or %(name)s placeholders (vars=Dict)
        :param vars: Iterable or Dict
        :return:
        """
        start_time = perf_counter()

        conn = local.conn # type: connection
        cursor = conn.cursor()

        # logger.debug(f"[{threading.current_thread().name}] Executing SQL: sql={sql}")
        try:
            cursor.execute(sql, vars)

            result = None
            if sql.split(maxsplit=1)[0].upper() == 'SELECT':
                result = cursor.fetchall()
            else:
                conn.commit()
        except Exception as e:
            logger.error(f"[{threading.current_thread().name}] Error executing SQL: error={e.__class__.__name__}, message={e}")
            conn.rollback()
            raise

        end_time = perf_counter()
        logger.debug(f"[{threading.current_thread().name}] Executing SQL: sql='{sql}' time={end_time - start_time:.3f}")

        return result

    def migrate(self, migration_dir: str, migrations_table_name: str = 'migrations'):
        # select the last 20 installed migrations
        sql = f"SELECT * FROM {migrations_table_name} ORDER BY id DESC LIMIT 20"
        try:
            result = self.execute(sql)
        except psycopg2.errors.UndefinedTable as e:
            self._create_migrations_table(migrations_table_name)
            result = self.execute(sql)

        already_applied_migration_ids = [r[0] for r in result]

        logger.debug(f"Last 20 migrations: {already_applied_migration_ids}")

        migration_files = sorted(listdir(migration_dir))
        for migration_file in migration_files:
            if not migration_file.endswith('.sql'):
                continue
            migration_id = migration_file.rsplit('.', maxsplit=1)[0]

            if migration_id in already_applied_migration_ids:
                continue

            logger.info(f"Applying migration {migration_id}")
            with open(f"{migration_dir}/{migration_file}") as f:
                sql = f.read()

            self.execute(sql)

            logger.info(f"Adding migration {migration_id} to {migrations_table_name}")
            sql = f"INSERT INTO {migrations_table_name} (id) VALUES ('{migration_id}')"
            self.execute(sql)


    def _create_migrations_table(self, migrations_table_name: str):
        sql = f"""
        CREATE TABLE {migrations_table_name} (
            id VARCHAR(255) PRIMARY KEY,
            applied_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.execute(sql)
