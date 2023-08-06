from typing import *

from .functional import autoimport


__all__ = 'get_json_encoder',


def get_json_encoder():
    from ..conf import settings

    return autoimport(settings.JSON_ENCODER)
