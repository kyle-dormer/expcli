#!/usr/bin/python3
"""
Author: Kyle Dormer
Date: 05/11/2019
Student Number: s1802423
"""

import sqlite3
from datetime import date as d
from datetime import datetime

connection = sqlite3.connect('expenses.db')
cursor = connection.cursor()


def db_init():
    cursor.execute('CREATE TABLE IF NOT EXISTS Expense(ID INTEGER NOT NULL PRIMARY \
                                                  KEY AUTOINCREMENT UNIQUE,   \
                                                  Date TEXT, Category TEXT,   \
                                                  Amount REAL)')

    cursor.execute('CREATE TABLE IF NOT EXISTS Month(Date TEXT NOT NULL \
            PRIMARY KEY UNIQUE, Budget REAL)')

    cursor.execute('CREATE TABLE IF NOT EXISTS Category(Name TEXT NOT NULL PRIMARY \
    KEY UNIQUE, Budget REAL)')

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Income(Name TEXT NOT NULL PRIMARY KEY UNIQUE, Amount REAL)')

    populate_months()


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
        cursor.execute(
            'SELECT * FROM Expense WHERE Category = (?)', (category,))
    elif category is None:
        cursor.execute('SELECT * FROM Expense')

    return cursor.fetchall()


def store_income_source(income_source):
    cursor.execute('INSERT INTO Income(Name, Amount) VALUES (?, ?)',
                   (income_source['source_name'], income_source['source_income']))

    connection.commit()


def store_income_sources(source_array):
    for source in source_array:
        cursor.execute('INSERT INTO Income(Name, Amount) VALUES (?, ?)',
                       (source['source_name'], source['source_income']))

    connection.commit()


def populate_months():
    cursor.execute('SELECT * FROM Month')

    if cursor.fetchone() == None:
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        years = [2019, 2020, 2021, 2022]

        for year in years:
            for month in months:
                date_stamp = str(month) + '-' + str(year)
                cursor.execute(
                    'INSERT INTO Month(Date) VALUES (?)', (date_stamp,))

        connection.commit()


def store_monthly_budget(budget):
    try:
        cursor.execute('UPDATE Month SET Budget = (?)', (budget,))
        connection.commit()
        print('Your new monthly budget was stored successfully!\n')
    except (Exception):
        print('There was an error storing your new monthly budget. Please try again!\n')


def store_categories(categories_array):
    try:
        for category in categories_array:
            cursor.execute('INSERT INTO Category(Name, Budget) VALUES (?, ?)',
                           (category['category_name'], category['category_budget']))
        connection.commit()
        print('Your expense categories have been stored successfully!\n')
    except (Exception):
        print('There was an error storing your expense categories. Please try again!\n')


def get_categories():
    cursor.execute('SELECT * FROM Category')

    categories = []

    for category in cursor.fetchall():
        categories.append(category[0])

    return categories
