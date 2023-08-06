from __future__ import annotations

import logging
import os
import time
from os.path import isfile, join

logger = logging.getLogger(__name__)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

class Manage:
    def __init__(self):
        import argparse
        parser = argparse.ArgumentParser(description='')

        parser.add_argument('command', metavar='COMMAND', type=str,
                            choices=["dev", "test"],
                            help='')

        self.args = parser.parse_args()

        print(self.args.command)

    def main(self):
        getattr(self, f"on_command_{self.args.command}")()

    def _get_app_dir(self):
        app_dir = None
        # find directories in current directory containing a main.py file, select the first one
        for directory in os.listdir("."):
            if not os.path.isdir(directory):
                continue
            if isfile(join(directory, "main.py")):
                app_dir = directory
                break

        if not app_dir:
            raise RuntimeError("No app directory found")

        return app_dir

    def on_command_dev(self):
        directory = self._get_app_dir()
        port = 20102

        import webbrowser
        def open_webbrowser():
            # ensure app is up
            time.sleep(2)

            url = f"http://localhost:{port}"
            print(f"Open {url} in your browser")
            webbrowser.open(url)

        import threading
        thread = threading.Thread(target=open_webbrowser)
        thread.start()

        cmd = ["uvicorn", f"{directory}.main:app", "--host", "0.0.0.0", "--port", str(port), "--reload"]
        print(" ".join(cmd))
        os.system(" ".join(cmd))


    def on_command_test(self):
        print("test")


def main():
    Manage().main()
