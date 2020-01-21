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
    """
    Initialise the database for the application by creating the tables and populating the month table.
    """
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
    """
    Close database connection.
    """
    cursor.close()
    connection.close()


def store_expense(expense):
    """
    Store the expense given as an argument in the database.
    """
    try:
        cursor.execute('INSERT INTO Expense(Date, Category, Amount) VALUES (?, ?, ?)',
                       (expense['date'], expense['category'], expense['amount']))
        print('Expense stored successfully!')
        connection.commit()
    except (Exception):
        print('There was an error storing your expense! Please try again!\n')


def get_expense(ID):
    """
    Get the expense with the corresponding ID from the database and return it.
    """
    cursor.execute('SELECT * FROM Expense WHERE ID=?', (ID,))
    expense = cursor.fetchone()
    return expense


def get_expenses(category):
    """
    Get all expenses from the database and return them.
    """
    if category:
        cursor.execute(
            'SELECT * FROM Expense WHERE Category = (?)', (category,))
    elif category is None:
        cursor.execute('SELECT * FROM Expense')

    return cursor.fetchall()


def store_income_source(income_source):
    """
    Store the source of income passed as an argument in the database.
    """
    cursor.execute('INSERT INTO Income(Name, Amount) VALUES (?, ?)',
                   (income_source['source_name'], income_source['source_income']))

    connection.commit()


def store_income_sources(source_array):
    """
    Store each income source in the source array passed in the database.
    """
    for source in source_array:
        cursor.execute('INSERT INTO Income(Name, Amount) VALUES (?, ?)',
                       (source['source_name'], source['source_income']))

    connection.commit()


def populate_months():
    """
    Populate the Month table of the database with all months for 2019 and 2020.
    """
    cursor.execute('SELECT * FROM Month')

    if cursor.fetchone() == None:
        months = ['01', '02', '03', '04', '05',
                  '06', '07', '08', '09', '10', '11', '12']
        years = ['2019', '2020']

        for year in years:
            for month in months:
                date_stamp = year + '-' + month
                cursor.execute(
                    'INSERT INTO Month(Date) VALUES (?)', (date_stamp,))

        connection.commit()


def store_monthly_budget(budget):
    """
    Set the monthly budget for each month in the database. Expected type is float.
    """
    try:
        cursor.execute('UPDATE Month SET Budget = (?)', (budget,))
        connection.commit()
        print('Your new monthly budget was stored successfully!\n')
    except (Exception):
        print('There was an error storing your new monthly budget. Please try again!\n')


def store_categories(categories_array):
    """
    Store each category in the categories_array argument in the database.
    """
    try:
        for category in categories_array:
            cursor.execute('INSERT INTO Category(Name, Budget) VALUES (?, ?)',
                           (category['category_name'], category['category_budget']))
        connection.commit()
        print('Your expense categories have been stored successfully!\n')
    except (Exception):
        print('There was an error storing your expense categories. Please try again!\n')


def get_categories():
    """
    Get all expense categories from the database and return them.
    """
    cursor.execute('SELECT * FROM Category')

    categories = []

    for category in cursor.fetchall():
        categories.append(category[0])

    return categories
