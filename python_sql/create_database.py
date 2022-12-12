#https://www.projectpro.io/recipes/connect-mysql-python-and-import-csv-file-into-mysql-and-create-table

import mysql.connector as msql
from mysql.connector import Error
from key import password_sql
from connectie_mysql import conn

def database_dhl():
    try:
        c = conn.cursor()
        c.execute("CREATE DATABASE dhl")
        print("database created")
    except Error as e:
        print("Error while connecting to MySQL", e)



#try:
    #The connect() constructor creates a connection to the MySQL server and returns a MySQLConnection object.
    #  conn = msql.connect(host='localhost', user='root', password=password_sql)#give ur username, password
    #if conn.is_connected():
        #The MySQLCursor of mysql-connector-python (and similar libraries) is 
        # used to execute statements to communicate with the MySQL database. 
        # Using the methods of it you can execute SQL statements, fetch 
        # data from the result sets, call procedures.
        #cursor = conn.cursor()
        #cursor.execute("CREATE DATABASE dhl")
        #print("Database is created")
#except Error as e:
    #print("Error while connecting to MySQL", e)