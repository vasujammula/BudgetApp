#!/usr/bin/python
import sqlite3
import os
import sys

db_location = "transactions.db"


class data_handler():
    def __init__(self):
        print "INFO:Checking and initializing database"
        if (os.path.exists(db_location)):
            pass
        # Schema for table #c.execute('''CREATE TABLE transactions(amount text, date text, type text)''')
        else:
            print "ERROR:Database Not Present "
            sys.exit(1)

    def add_trans(self, amount, date, ttype):
        conn_h = sqlite3.connect(db_location)
        if (conn_h):
            c_h = conn_h.cursor()
            if c_h:
                c_h.execute("INSERT INTO transactions VALUES ('%s','%s','%s')" % (amount, date, ttype))
                conn_h.commit()
                conn_h.close()
            else:
                print "ERROR:ERROR WHILE INSERTING"
        else:
            print "ERROR:ERORR WHILE OPENEING DATABASE"

    def view_trans(self):
        rows = ""
        conn_h = sqlite3.connect(db_location)
        conn_h.text_factory = str
        if (conn_h):
            c_h = conn_h.cursor()
            if c_h:
                c_h.execute("SELECT * FROM transactions ")
                rowst = c_h.fetchall()

                for row in rowst:
                    rows = rows + "\n" + str(row)
                print rows
            else:
                print "ERROR:ERROR WHILE INSERTING"
        else:
            print "ERROR:ERORR WHILE OPENEING DATABASE"
        conn_h.close()
        return rows


if __name__ == "__main__":
    d = data_handler()
    # d.add_trans("3000","may17","D")
    d.view_trans()
