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
import os
import mysql.connector


PII_FIELDS = ('email', 'name', 'password', 'ssn', 'phone')


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
    handler = logging.StreamHandler()

    # Create formatter
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database

    Returns:
        _type_: mysql.connector.connection.MySQLConnection
    """
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_passwd = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')

    conn = mysql.connector.connect(
        host=db_host,
        user=db_username,
        password=db_passwd,
        database=db_name,
        port=3306
    )

    return conn


def main() -> None:
    conn = get_db()
    cur = conn.cursor
    
    cur.execute('SELECT * FORM users')
    users = cur.fetchall()
    # logger = get_logger()
    # handler = logging.StreamHandler()
    
    # formatter = RedactingFormatter()
    for user in users:
        print(user)
        
    
    
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
