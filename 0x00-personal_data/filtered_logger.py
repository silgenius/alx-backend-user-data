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

from re import sub, escape as esc


def filter_datum(flds, rdt, msg, spr):
    """a function called that returns the log message obfuscated"""
    for fld in flds:
        msg = sub(esc(fld) + r"=" + r"[^" + spr + r"]+", f'{fld}={rdt}', msg)
    return msg
