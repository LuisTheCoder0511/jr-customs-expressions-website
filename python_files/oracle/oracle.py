import threading

import oracledb
import time

username = 'ADMIN'
password = '!JessieR!2002'
service = 'g07567ddef9372a_jrcustomsexpressions_low.adb.oraclecloud.com'
service_name = 'jrcustomsexpressions_low'
dsn = "(description= (retry_count=3)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.us-ashburn-1.oraclecloud.com))(connect_data=(service_name=g07567ddef9372a_jrcustomsexpressions_low.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"

local_string = f"localhost:1522/{service_name}"


class Database:
    def __init__(self):
        self.terminate = False
        self.open = True
        self.connection: oracledb.Connection

    def __open__(self):
        self.idle_time = int(time.time())
        if self.open:
            self.open = False

            print(f"Connecting to Oracle database...")
            self.connection = oracledb.connect(user=username, password=password, dsn=dsn)
            print(f"Connection is open!")

        self._cursor = self.connection.cursor()

    def __idle_time_check__(self):
        while not self.terminate:
            time.sleep(10)
            current_time = int(time.time())
            if current_time - self.idle_time >= 360:
                self.__close__()

    def __close__(self):
        if self.open:
            return
        print(f"Disconnecting from Oracle database...")
        self.connection.close()
        self.connection = None
        self.open = True
        print("Connection is closed!")

    def __drop_table__(self, table_name: str):
        self.__open__()
        self.__execute__(f"DROP TABLE {table_name}")

    def __row_factory__(self):
        self.__open__()
        self._cursor.rowfactory = lambda cursor, row: row

    def __fetch_one__(self):
        return self._cursor.fetchone()

    def __fetch_all__(self):
        return self._cursor.fetchall()

    def __execute__(self, statement: str, params: tuple = None):
        self.__open__()
        try:
            if params is None:
                self._cursor.execute(statement)
            else:
                self._cursor.execute(statement, params)
            self.connection.commit()
        except Exception as e:
            print(e)
            print(e.args)
            return False
        return True


database = Database()


def __run__():
    database.__open__()
    thread = threading.Thread(target=database.__idle_time_check__)
    thread.daemon = True
    thread.start()


def __stop__():
    database.terminate = True
    database.__close__()
