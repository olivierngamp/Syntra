from key import password_sql #dit is een klasse die ik heb gemaakt en mijn password in zit als een variable
import mysql.connector as msql
from mysql.connector import Error

def create_connection(host, user, db):
    conn = None
    try:
        conn = msql.connect(host=host, user=user, password=password_sql, database = db)
        return conn
    except Error as e:
        print("Error while connecting to MySQL", e)

    return conn
