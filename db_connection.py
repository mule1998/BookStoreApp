import mysql.connector as connector
from dotenv import load_dotenv
import os
import logging

load_dotenv()
logging.basicConfig(filename='user.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')


class DatabaseConnection:

    @staticmethod
    def dbconnection():
        con = connector.connect(host='localhost', port='3306', user=os.getenv('user'),
                                     password=os.getenv('passwrd'),
                                     database='book_store')
        return con
    logging.info("Database Connection is Established")


# conn_1 = DatabaseConnection()
# conn_1.dbconnection()
