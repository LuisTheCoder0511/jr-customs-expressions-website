import threading
import time
import os

import oracledb

service_name = "jrcustomsexpressions_low"
service = f"g07567ddef9372a_{service_name}.adb.oraclecloud.com"
dsn = f"(description=(retry_count=3)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.us-ashburn-1.oraclecloud.com))(connect_data=(service_name={service}))(security=(ssl_server_dn_match=yes)))"

class Database:
    def __init__(self, username):
        self._terminate = False
        self._closed = True
        self._connection: oracledb.Connection
        self._username = username

    def _connect(self):
        self._password = os.getenv("ORACLE_KEY")

    def _open(self):
        self.idle_time = int(time.time())
        tries = 0
        while self._closed and tries < 3:
            try:
                print(f"Connecting to Oracle database...")
                self._connect()
                self._connection = oracledb.connect(user=self._username, password=self._password, dsn=dsn)
                print(f"Connection is open!")
                self._closed = False
            except Exception as e:
                print(f"Failed to connect to Oracle database: {e}")
                tries += 1
        self._cursor = self._connection.cursor()

    def _idle_check(self):
        while not self._terminate:
            time.sleep(10)
            current_time = int(time.time())
            if current_time - self.idle_time >= 360:
                self._close()

    def _close(self):
        if self._closed:
            return
        print(f"Disconnecting from Oracle database...")
        self._connection.close()
        self._closed = True
        self._password = ""
        print("Connection is closed!")

    def __row_factory__(self):
        self._open()
        self._cursor.rowfactory = lambda cursor, row: row

    def __fetch_one__(self):
        return self._cursor.fetchone()

    def __fetch_all__(self):
        return self._cursor.fetchall()

    def __execute__(self, statement: str, params: tuple = None):
        self._open()
        print(f"\nStatement:\n{statement}\n")
        try:
            if params is None:
                self._cursor.execute(statement)
            else:
                self._cursor.execute(statement, params)
            self._connection.commit()
        except Exception as e:
            print(e)
            print(e.args)
            return False
        return True

    def run(self):
        self._open()
        thread = threading.Thread(target=self._idle_check)
        thread.daemon = True
        thread.start()

    def terminate(self):
        self._terminate = True
        self._close()

database = Database("ADMIN")

def __run__():
    database.run()

def __stop__():
    database.terminate()
