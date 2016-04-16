#!/usr/bin/python

"""@db_query

This file contains various generic SQL-related methods.
"""

import MySQLdb as DB
from log.logger import Logger
from brain.database.db_settings import Database


class SQL(object):
    """@SQL

    This class provides an interface to connect, execute commands, and
    disconnect from a SQL database.  It explicitly inherits pythons 'new-style'
    class.

    Note: this class is invoked within 'save_xx.py', and 'retrieve_xx.py'
          modules.

    Note: this class explicitly inherits the 'new-style' class.

    """

    def __init__(self, host=None, user=None, passwd=None):
        """@__init__

        This constructor is responsible for defining class variables.

        """

        self.db_settings = Database()
        self.list_error = []
        self.proceed = True

        # database logger
        self.logger = Logger('database', 'database', 'debug')

        # host address
        if host:
            self.host = host
        else:
            self.host = self.db_settings.get_db_host()

        # sql username for above host address
        if user:
            self.user = user
        else:
            self.user = self.db_settings.get_db_username()

        # sql password for above username
        if passwd:
            self.passwd = passwd
        else:
            self.passwd = self.db_settings.get_db_password()

    def sql_connect(self, database=None):
        """@sql_connect

        This method is responsible for defining the necessary interface to
        connect to a SQL database.

        """

        try:
            if database is None:
                self.conn = DB.connect(
                    self.host,
                    self.user,
                    self.passwd,
                )
            else:
                self.conn = DB.connect(
                    self.host,
                    self.user,
                    self.passwd,
                    db=database,
                )
            self.cursor = self.conn.cursor()

            # log successful connection
            if (self.cursor):
                self.logger.debug('database connected: success')

            return {
                'status': True,
                'error': None,
                'id': None,
            }

        except DB.Error, error:
            self.proceed = False
            self.list_error.append(error)

            # log unsuccessful connection
            if (self.cursor):
                self.logger.debug('database connected: fail')

            return {
                'status': False,
                'error': self.list_error,
                'id': None,
            }

    def sql_command(self, sql_statement, sql_type, sql_args=None):
        """@sql_connect

        This method is responsible for defining the necessary interface to
        perform SQL commands.

        @sql_args, is a tuple used for argument substitution with the supplied
            'sql_statement'.
        """

        if self.proceed:
            try:
                self.cursor.execute(sql_statement, sql_args)

                # commit change(s), return lastrowid
                if sql_type in ['insert', 'delete', 'update']:
                    self.conn.commit()
                # fetch all the rows, return as list of lists.
                elif sql_type == 'select':
                    result = self.cursor.fetchall()

                # log transaction
                arguments = sql_args if sql_args else 'None'
                self.logger.debug('transaction: success, statement: ' + sql_statement + ', arguments: ' + arguments)

            except DB.Error, error:
                self.conn.rollback()
                self.list_error.append(error)
                return {
                    'status': False,
                    'error': self.list_error,
                    'result': None,
                }

                # log transaction
                arguments = sql_args if sql_args else 'None'
                self.logger.debug('transaction: success, statement' + sql_statement + ', arguments: ' + arguments)

        if sql_type in ['insert', 'delete', 'update']:
            return {
                'status': False,
                'error': self.list_error,
                'id': self.cursor.lastrowid,
            }
        elif sql_type == 'select':
            return {
                'status': False,
                'error': self.list_error,
                'result': result,
            }

    def sql_disconnect(self):
        """@sql_disconnect

        This method is responsible for defining the necessary interface to
        disconnect from a SQL database.

        """

        if self.proceed:
            try:
                if self.conn:
                    self.conn.close()

                    # log disconnection
                    self.logger.debug('database disconnected: success')

                    return {
                        'status': True,
                        'error': None,
                        'id': self.cursor.lastrowid,
                    }
            except DB.Error, error:
                self.list_error.append(error)

                # log disconnection
                self.logger.debug('database disconnected: fail')

                return {
                    'status': False,
                    'error': self.list_error,
                    'id': self.cursor.lastrowid,
                }

    def get_errors(self):
        """@get_errors

        This method returns all errors pertaining to the instantiated class.

        """

        return self.list_error
