#!/usr/bin/env python3

"""
Module for obfuscating specified fields in log messages.

Provides a function to replace sensitive fields in a log message with
a redaction string. The fields to obfuscate, redaction, and separator
are customizable.

Functions:
    filter_datum(fields, redaction, message, separator):
    Obfusates specified fields in a log message.
"""

from re import escape as esc
import re
from typing import List


def filter_datum(flds: List, rdt: str, msg: str, spr: str) -> str:
    """a function called that returns the log message obfuscated"""
    for fd in flds:
        msg = re.sub(esc(fd) + r"=" + r"[^" + spr + r"]+", f'{fd}={rdt}', msg)
    return msg
