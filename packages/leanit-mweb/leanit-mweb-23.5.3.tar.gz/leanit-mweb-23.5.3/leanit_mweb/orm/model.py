from __future__ import annotations
import logging
from pprint import pprint

from leanit_mweb import YugabytedbThreadPool
from leanit_mweb.orm.fields import Field
from leanit_mweb.utils import camelCaseToSnakeCase

logger = logging.getLogger(__name__)

from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    pass

class Model:
    _db: YugabytedbThreadPool = None
    _table = None
    _pk = None

    fields = {}

    def __init__(self, **kwargs):
        self._created = False
        # shows the difference between the initial values and the current values
        # {"name": ("old name", "new name")}
        self._diff = {}

        # dict of initial values
        self._init_values = kwargs

        # set attributes
        for field_name, field_instance in self.fields.items():
            if value := kwargs.get(field_name):
                setattr(self, field_name, value)
            else:
                setattr(self, field_name, field_instance.get_default())

    @classmethod
    def create(cls, **kwargs) -> "cls":
        insert_doc = {}

        for field_name, field_instance in cls.fields.items():
            if value := kwargs.get(field_name):
                insert_doc[field_name] = field_instance.to_db(value)
            else:
                value = field_instance.get_default()
                if value is not None:
                    insert_doc[field_name] = value
                    # logger.debug(f"field_name: {field_name}, value: {value}")

        instance = cls(**insert_doc)

        sql = f"INSERT INTO \"{cls._table}\" ({','.join(insert_doc.keys())}) VALUES ({','.join(['%s'] * len(insert_doc))})"
        # logger.debug(f"SQL: {sql}")

        instance.on_pre_create()
        cls._db.execute(sql, tuple(insert_doc.values()))
        instance._created = True
        instance.on_post_create()

        return instance

    @classmethod
    def get(cls, _only=None, **kwargs) -> "cls":
        result = cls.filter(_only=_only, _limit=1, **kwargs)
        if result:
            return result[0]
        else:
            return None

    @classmethod
    def filter(cls, _only=None, **kwargs):
        field_names = [*cls.fields.keys()]

        sql, values = cls._get_select_query_and_values(_only=field_names, **kwargs)
        # logger.debug(f"SQL: {sql}")

        result = []

        rows = cls._db.execute(sql, values)
        for row in rows:
            instance = cls(**dict(zip(field_names, row)))
            instance._created = True

            result.append(instance)

        # logger.debug(f"result: {result}")

        return result

    @classmethod
    def _get_select_query_and_values(cls, _only=None, _limit=None, **kwargs):
        operators = {
            "gt": ">",
            "lt": "<",
            "gte": ">=",
            "lte": "<=",
            "ne": "!="
        }
        conditions = []
        values = []
        for key, value in kwargs.items():
            if "__" in key:
                column, op = key.split("__")
                op = operators[op]
            else:
                column = key
                op = "="
            conditions.append(f"{column}{op}%s")
            values.append(value)
        conditions = " AND ".join(conditions)
        if _only:
            columns = ",".join(_only)
        else:
            columns = "*"
        query = f"SELECT {columns} from \"{cls._table}\" where {conditions}"
        if _limit:
            query += f" LIMIT {_limit}"
        return [query, values]

    @classmethod
    def _initialize(cls):
        # initialize fields, this is required
        # otherwise the fields are getting written into the same dict of the parent class
        # Model.fields
        cls.fields = {}

        for field_name, field_instance in cls.__dict__.items():
            if isinstance(field_instance, Field):
                cls.fields[field_name] = field_instance
                field_instance.name = field_name

        if not cls._table:
            # camel cast to snake case with under score
            cls._table = camelCaseToSnakeCase(cls.__name__)

        from leanit_mweb import db
        cls._db = db

        # check for primary key
        if not cls._pk:
            raise Exception(f"Primary key `_pk` not defined for '{cls.__name__}'")
        if type(cls._pk) == str:
            cls._pk = [cls._pk]

    def __str__(self):
        result = f"{self.__class__.__name__}("
        for field_name, field_instance in self.fields.items():
            result += f"{field_name}={getattr(self, field_name)},"
        result += ")"
        return result

    def save(self):
        self._diff = {}

        if self._created:
            # update
            update_doc = {}

            for field_name, old_value in self._init_values.items():
                new_value = getattr(self, field_name)
                if old_value != new_value:
                    update_doc[field_name] = new_value
                    self._diff[field_name] = (old_value, new_value)
                    # update init values
                    self._init_values[field_name] = new_value

            if not update_doc:
                # nothing to update, do not fire update events
                return

            self.on_pre_update()

            if update_doc:
                sql, values = self._get_update_query_and_values(update_doc)

                # logger.debug(f"SQL: {sql}")

                self._db.execute(sql, values)

            self.on_post_update()

        else:
            # create
            create_doc = {}
            for field_name, field_instance in self.fields.items():
                value = getattr(self, field_name)
                if value is not None and not isinstance(value, Field):
                    create_doc[field_name] = value

            self.create(**create_doc)
            self._created = True

        # ensure that the diff is empty
        self._diff = {}


    def _get_update_query_and_values(self, update_doc: Dict):
        set_values = []
        set_args = []
        for key, value in update_doc.items():
            set_values.append(f"{key}=%s")
            set_args.append(value)
        set_values = ",".join(set_values)

        where_values = []
        where_args = []
        for key in self._pk:
            where_values.append(f"{key}=%s")
            where_args.append(getattr(self, key))
        where_values = " AND ".join(where_values)

        query = f"UPDATE \"{self._table}\" SET {set_values} WHERE {where_values}"
        args = set_args + where_args
        return [query, args]

    def on_pre_create(self):
        pass

    def on_post_create(self):
        pass

    def on_pre_update(self):
        pass

    def on_post_update(self):
        pass

    def on_pre_delete(self):
        pass

    def on_post_delete(self):
        pass
