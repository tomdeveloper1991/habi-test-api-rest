import mysql.connector
import configparser

CONTEXT = "prd"


class MsqlAdapter():
    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read("conf.ini")
        print(config.sections())
        self.connection = mysql.connector.connect(
            host=config[CONTEXT]["host"],
            port=int(config[CONTEXT]["port"]),
            database=config[CONTEXT]["database"],
            user=config[CONTEXT]["user"],
            password=config[CONTEXT]["password"]
        )

    def open_connection(self) -> mysql.connector.MySQLConnection:
        if self.connection.is_connected():
            return self.connection

    def close_connection(self) -> None:
        if self.connection.is_connected():
            self.connection.close()
