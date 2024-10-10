import mysql.connector
from dotenv import load_dotenv
import os

class DatabaseConnection:

    def __init__(self):
        load_dotenv()
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.DB_NAME = os.getenv('DB_NAME')
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.DB_HOST,
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                database=self.DB_NAME,
                autocommit=True
            )
            if self.connection.is_connected():
                print("Successfully connected to database")
            else:
                print("Failed to connect to database")
        except mysql.connector.Error as e:
            print('Error connecting to database:', e)

    def get_cursor(self):
        if not self.cursor:
            self.cursor = self.connection.cursor(dictionary=True)
        return self.cursor

    def close(self):
        if self.cursor:
            self.cursor.close()
            print("Cursor closed successfully")
        if self.connection:
            self.connection.close()
            print("Connection closed successfully")
