"""
Author: Kyle Dormer
Date: 05/11/2019
Student Number: s1802423
"""

import sqlite3

conn = sqlite3.connect('expenses.db')
c = conn.cursor()


def db_init():
    c.execute('CREATE TABLE IF NOT EXISTS Expense(ID INTEGER NOT NULL PRIMARY \
                                                  KEY AUTOINCREMENT UNIQUE,   \
                                                  Date TEXT, Category TEXT,   \
                                                  Amount REAL)')

    c.execute('CREATE TABLE IF NOT EXISTS Month(Date INTEGER NOT NULL \
            PRIMARY KEY UNIQUE, Budget REAL)')

    c.execute('CREATE TABLE IF NOT EXISTS Category(Name TEXT NOT NULL PRIMARY \
    KEY UNIQUE, Budget REAL)')


def db_close():
    c.close()
    conn.close()
