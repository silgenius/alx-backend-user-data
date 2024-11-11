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

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                message: str, separator: str) -> str:
    """a function called that returns the log message obfuscated"""
    pattern = r'(' + '|'.join(fields) + r')=(.*?)(' + separator + '|$)'
    return re.sub(pattern, r'\1=' + redaction + r'\3', message)
