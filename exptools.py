#!/usr/bin/python3
"""
Author: Kyle Dormer
Date: 27/10/2019
Student Number: s1802423
"""

from datetime import datetime
import pandas as pd
import expsql as sql
import matplotlib as plt


def validate_input(user_input, lower_length, upper_length, desired_type):
    """
    Used for validating user input. It takes the user's input, the lowest
    acceptable length, the highest acceptable length and the desired type of input. It then returns a boolean according to whether the user's input matches the given length range and type.
    """
    return ((len(user_input) >= lower_length) and
            (len(user_input) <= upper_length)) and \
        type(user_input) == desired_type


def validate_date(date_string):
    """
    Validate data string passed as argument to ensure user inputted data conforms to correct format.
    """
    date_format = '%Y-%m-%d'

    try:
        datetime_object = datetime.strptime(date_string, date_format)

        if datetime_object:
            return True

    except (ValueError):
        return False


def get_week(date_string):
    if validate_date(date_string):
        try:
            datetime_object = datetime.strptime(date_string, '%Y-%m-%d')
            return datetime_object.isocalendar()[1]
        except (TypeError):
            return False


def get_year(date_string):
    if validate_date(date_string):
        try:
            datetime_object = datetime.strptime(date_string, '%Y-%m-%d')
            return datetime_object.isocalendar()[0]
        except (TypeError):
            return False


def get_average_expenses(expense_array):
    categories = []

    for expense in expense_array:
        if not any(category['Category'] == expense[2] for category in categories):
            categories.append(
                {'Category': expense[2], 'Total': 0, 'Average': 0, 'Budget': None})

    for category in categories:
        expense_count = 0
        budget = sql.get_budget(category['Category'])

        for expense in expense_array:
            if expense[2] == category['Category']:
                category['Total'] += expense[3]
                expense_count += 1

        category['Average'] = category['Total'] / expense_count

        try:
            if category['Total'] > budget[0]:
                category['Budget'] = 'Over'
            else:
                category['Budget'] = 'Under'
        except (TypeError):
            category['Budget'] = 'None'

        expense_count = 0

    return categories


def export_csv():
    expenses = sql.get_expenses(None)

    if expenses:
        try:
            data_frame = pd.DataFrame(expenses)
            data_frame.to_csv('expenses.csv')
            print('Expenses exported successfully!\n')
        except (Exception):
            print(
                'There was an error exporting your expenses to a CSV file! Please try again!\n')
    else:
        print(
            'There was an error exporting your expenses to a CSV file! Please try again! Please ensure you have some categories and expenses stored!\n')


def export_pdf():
    expenses = sql.get_expenses(None)

    if expenses:
        try:

            average_expenses = get_average_expenses(expenses)

            data_frame = pd.DataFrame(average_expenses)
            data_frame.set_index('Category', drop=True, inplace=True)

            plot = data_frame.plot(kind='bar')
            plt.pyplot.tight_layout()
            plt.pyplot.savefig('expenses.pdf')

            print_important('Your expenses were successfully exported to PDF!')
        except (Exception):
            print_important(
                'There was an error exporting your expenses! Please ensure you have both some expenses and expense categories saved!')
    else:
        print_important(
            'There was an error exporting your expenses! Please ensure you have both some expenses and expense categories saved!')


def print_important(string):
    print('\n')
    print(string)
    print('\n')
