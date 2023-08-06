from __future__ import annotations
import logging

logger = logging.getLogger(__name__)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def camelCaseToSnakeCase(name):
    return ''.join(['_'+i.lower() if i.isupper() else i for i in name]).lstrip('_')
