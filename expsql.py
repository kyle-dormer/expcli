#!/usr/bin/python3
"""
Author: Kyle Dormer
Date: 05/11/2019
Student Number: s1802423
"""

import sqlite3
from datetime import date as d

connection = sqlite3.connect('expenses.db')
cursor = connection.cursor()


def db_init():
    cursor.execute('CREATE TABLE IF NOT EXISTS Expense(ID INTEGER NOT NULL PRIMARY \
                                                  KEY AUTOINCREMENT UNIQUE,   \
                                                  Date TEXT, Category TEXT,   \
                                                  Amount REAL)')

    cursor.execute('CREATE TABLE IF NOT EXISTS Month(Date INTEGER NOT NULL \
            PRIMARY KEY UNIQUE, Budget REAL)')

    cursor.execute('CREATE TABLE IF NOT EXISTS Category(Name TEXT NOT NULL PRIMARY \
    KEY UNIQUE, Budget REAL)')

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Income(Name TEXT NOT NULL PRIMARY KEY UNIQUE, Amount REAL)')


def db_close():
    cursor.close()
    connection.close()


def store_expense(date, category, amount):
    if date is None:
        date = d.today()

    cursor.execute(
        'INSERT INTO Expense(Date, Category, Amount) VALUES (?, ?, ?)', (date, category, amount))

    connection.commit()


def get_expense(ID):
    cursor.execute('SELECT * FROM Expense WHERE ID=?', (ID,))
    expense = cursor.fetchone()
    return expense


def get_expenses(category):
    if category:
        cursor.execute('SELECT * FROM Expense WHERE Category=?', (category,))
    elif category is None:
        cursor.execute('SELECT * FROM Expense')

    return cursor.fetchall()


db_init()
