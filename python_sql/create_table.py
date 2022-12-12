import mysql.connector as msql
from mysql.connector import Error
from key import password_sql 
from connectie_mysql import create_connection

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():

    sql_create_departement_table = """ 
                                        CREATE TABLE IF NOT EXISTS departement (
                                        DEPARTEMENT_ID int(6) NOT NULL AUTO_INCREMENT,
                                        DEPARTEMENT varchar(30),
                                        Primary Key(DEPARTEMENT_ID))
                                  """

    sql_create_techniekers_table = """  CREATE TABLE IF NOT EXISTS techniekers (
                                        TECHNIEKERS_ID int(6) NOT NULL AUTO_INCREMENT,
                                        DEPARTEMENT_ID int(6),
                                        NAAM varchar(30) DEFAULT NULL,
                                        GEB_DATUM Date,
                                        STRAAT varchar(15),
                                        HUISNR varchar(4),
                                        POSTCODE varchar(6),
                                        PLAATS varchar(15),
                                        TELEFOON varchar(10),
                                        primary key(TECHNIEKERS_ID),
                                        foreign key(DEPARTEMENT_ID) references departement (DEPARTEMENT_ID))
                                    """
    
    sql_create_sancties_table =      """ CREATE TABLE IF NOT EXISTS sancties (
                                        SANCTIE_ID int(6) NOT NULL AUTO_INCREMENT,
                                        SANCTIE_TYPE varchar(10),
                                        primary key(SANCTIE_ID))
                                    """
    sql_create_sanctieTechniekers_table =  """ CREATE TABLE IF NOT EXISTS sancties_technieker (
                                        TECHNIEKERS_ID int(6),
                                        SANCTIE_ID int(6),
                                        COMMENTAAR varchar(30),
                                        DATUM date,
                                        primary key(TECHNIEKERS_ID),
                                        primary Key(SANCTIE_ID))
                                    """
    sql_create_opleiding_table =  """CREATE TABLE IF NOT EXISTS opleiding (
                                        OPLEIDING_ID int(6) NOT NULL AUTO_INCREMENT,
                                        TITEL varchar(30),
                                        BEGIN_DATUM date,
                                        EIND_DATUM date,
                                        AANTAL_UREN int(6),
                                        primary key(OPLEIDING_ID))
                                    """
    sql_create_opl_technieker_table =  """ CREATE TABLE IF NOT EXISTS opleiding_technieker (
                                        TECHNIEKERS_ID int(6),
                                        OPLEIDING_ID int(6),
                                        COMMENTAAR varchar(30),
                                        primary key(TECHNIEKERS_ID),
                                        primary Key(OPLEIDING_ID))
                                    """

    conn = create_connection("localhost","root","dhl")

    if conn is not None:
        print("Connectie succes")
        print("Creating tables")
        create_table(conn, sql_create_departement_table)
        create_table(conn, sql_create_techniekers_table)
        create_table(conn, sql_create_sancties_table)
        create_table(conn, sql_create_sanctieTechniekers_table)
        create_table(conn, sql_create_opleiding_table)
        create_table(conn, sql_create_opl_technieker_table)
        
        

    else:
        print("Error! cannot create the database connection.")

main()