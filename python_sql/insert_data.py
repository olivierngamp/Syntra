import json
from connectie_mysql import create_connection
import mysql.connector as msql


c  = create_connection("localhost","root","dhl")

if c.is_connected():

        cursor = c.cursor()
        f = open('techniekers.json')  
        data = json.load(f)
        for i in data:
            departement_id = i["DEPARTEMENT_ID"]
            naam = i["NAAM"]
            geb_datum = i["GEB_DATUM"]
            straat = i["STRAAT"]
            huisnr = i["HUISNR"]
            postcode = i["POSTCODE"]
            plaats = i["PLAATS"]
            telefoon = i["TELEFOON"]

            query = f'''INSERT INTO techniekers(DEPARTEMENT_ID,naam, geb_datum, straat, huisnr, postcode, plaats, telefoon) VALUES(%s,%s, %s, %s, %s, %s, %s, %s);'''
            val = (departement_id, naam,geb_datum,straat, huisnr, postcode, plaats, telefoon)
            cursor.execute(query,val)

        c.commit()
        c.close()