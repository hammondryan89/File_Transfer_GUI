import sqlite3
import datetime 
import time




conn = sqlite3.connect('modified.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS file_check(id INTEGER PRIMARY KEY AUTOINCREMENT, datestamp TEXT NOT NULL)")
conn.commit()

def dataEntry():
        now = datetime.datetime.now()
        date = now.strftime('%Y-%m-%d %H:%M:%S')
        print (date) 
        c.execute("INSERT INTO file_check (datestamp) VALUES ('{}')".format(date))
        conn.commit()

def time_grab():
        c.execute("SELECT datestamp FROM file_check ORDER BY datestamp DESC LIMIT 1")
        sql = str(c.fetchone())
        return str(sql).replace('(', '').replace('u\'', '').replace(')', '').replace(',', '').replace("'", '')

def close():
        c.close()






