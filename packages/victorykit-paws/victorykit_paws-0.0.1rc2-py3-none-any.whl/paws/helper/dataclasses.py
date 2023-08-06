#!/usr/bin/env python3
"""
"""
from typing import Optional
from dataclasses import fields

from paws.helper.logging import get_default_logger


logger = get_default_logger(__name__)


def sanitize(proto: dict, cls: type, strict: Optional[bool] = False) -> dict:
    """
    """

    fields_ = {f.name: f.type for f in fields(cls)}

    field_names = fields_.keys()

    sanitized_proto = {}

    for k, v in proto.items():

        if k not in field_names:

            continue

        if not isinstance(v, fields_[k]):

            msg = '%s[%s]: received %s, expected %s' % (cls.__name__, k, v, fields_[k].__name__)

            if strict:

                raise TypeError(msg)

            else:

                logger.warn(msg)

        sanitized_proto[k] = v

    return sanitized_proto


def sanitize2(proto: dict) -> dict:
    """
    """

    return {k:v for k, v in proto.items() if v != None}