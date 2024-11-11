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
import logging


PII_FIELDS = ('ssn', 'password', 'ip', 'last_login', 'user_agent',)


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    """a function called that returns the log message obfuscated"""
    pattern = r'(' + '|'.join(fields) + r')=(.*?)(' + separator + '|$)'
    return re.sub(pattern, r'\1=' + redaction + r'\3', message)


def get_logger() -> logging.Logger:
    """
    logging.Logger object.
    """

    # Setting Up logger
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create handler
    handler = logging.streamHandler()

    # Create formatter
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ method to filter values in incoming log records"""
        msg = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
