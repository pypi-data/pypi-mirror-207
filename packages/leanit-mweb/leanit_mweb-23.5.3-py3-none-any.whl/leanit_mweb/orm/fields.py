from __future__ import annotations
import logging
import re

from ulid import ULID

from leanit_mweb.orm.exception import ValidationFailedException

logger = logging.getLogger(__name__)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class Field:
    def to_db(self, value):
        return value

    def get_default(self):
        return None

    def validate(self, value):
        """
        might raise ValidationFailedException
        :param value:
        :return:
        """
        pass


class IntegerField(Field):
    pass


class StringField(Field):
    pass


class EmailField(StringField):
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

    def validate(self, value):
        # validate email
        if not self.pattern.match(value):
            raise ValidationFailedException(f"Invalid email: '{value}'")



class UlidField(StringField):
    def get_default(self):
        return str(ULID())


class DateTimeField(Field):
    pass
