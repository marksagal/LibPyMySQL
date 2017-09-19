"""
LibPy/MySQL

@author:  sagal <mark@sagal.biz>
@version: 1.0.0
@since:   2017-09-19
"""
import warnings

try:
    import pymysql
except ImportError as import_error:
    warnings.warn(str(import_error))
    import pymysql


class MySQL(object):
    def __init__(self, db_name, db_user, db_pass='', db_host='localhost', db_port=3306, show_warnings=False):
        """
        Initialize database
        @param db_name: Database name
        @param db_user: Database user
        @param db_pass: Database pass (default '')
        @param db_host: Database host (default 'localhost')
        @param db_port: Database port (default 3306)
        """
        self.__show_warnings = show_warnings
        try:
            self.__connection = pymysql.connect(db=db_name,
                                                user=db_user,
                                                passwd=db_pass,
                                                host=db_host,
                                                port=db_port)
            self.__cursor = self.__connection.cursor()
        except Exception as exception:
            self.__warnings(exception)
            self.__connection = None

    def __enter__(self):
        """
        Initialize with with
        @return: <class 'MySQL'>
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Terminate with with
        """
        self.close()

    def query(self, query_str):
        """
        Execute queries
        @param query_str: Query string
        @return: <class 'pymysql.cursors.Cursor'>
        """
        if self.__connection is not None:
            try:
                self.__cursor.execute(query_str)
                return self.__cursor
            except Exception as exception:
                self.__warnings(exception)

    def close(self):
        """
        Terminate connections
        """
        if self.__connection is not None:
            self.__connection.commit()
            self.__cursor.close()
            self.__connection.close()

    def escape(self, raw_value):
        """
        Escape raw value to prevent mysql injections
        @param raw_value: Provide raw value to escape
        @return: Returns mysql escaped value
        """
        if self.__connection is not None:
            return self.__connection.escape(raw_value)
        return raw_value

    def rollback(self):
        """
        Rollback changes
        """
        if self.__connection is not None:
            self.__connection.rollback()

    def __warnings(self, exception):
        """
        Handle warnings
        @param exception: <class 'Exception'>
        @return: <type 'bool'>
        """
        if self.__show_warnings is True:
            warnings.warn(str(exception))
        return self.__show_warnings
