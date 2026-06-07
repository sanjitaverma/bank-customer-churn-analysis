import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bts@army2007",
        database="bank_churn"
    )
    return connection