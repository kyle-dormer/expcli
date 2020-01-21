#!/usr/bin/python3
"""
Author: Kyle Dormer
Date: 27/10/2019
Student Number: s1802423
"""

import sys
import exptools as ex
import expsql as sql


def main():
    sql.db_init()
    display_options()


def exit_handler():
    sql.db_close()
    print('Have a great day!')


def get_income():
    income_sources = get_income_sources([])
    monthly_income_total = 0

    for income_source in income_sources:
        monthly_income_total += income_source['source_income']

    try:
        sql.store_income_sources(income_sources)
        print('Income sources stored successfully!\n')
    except (Exception):
        print('There was an error while storing your income. Please try again!\n')


def get_income_sources(income_sources_list):
    """
    Recursively collects sources of income from the user and returns them in a
    list of dictionaries.
    """
    source_name = input('What is the name of the income source? ')

    if ex.validate_input(source_name, 1, 12, str):
        source_income = input('What is the monthly income of the source? ')

        try:
            source_income = float(source_income)
            income_sources_list.append({'source_name': source_name,
                                        'source_income': source_income})
            repeat = input('Enter another input source? [Y/n]\n')

            if repeat.lower() == 'y':
                get_income_sources(income_sources_list)

        except (Exception):
            print('Invalid input! That\'s not a valid number!')
            get_income_sources(income_sources_list)

    else:
        print('Invalid input! Your name is too big or too small!')
        get_income_sources(income_sources_list)

    return income_sources_list


def get_categories(categories_list):
    """
    Recursively collects categories of expense from the user and returns them
    in a list of dictionaries.
    """
    category_name = input('What is the name of the expense category? ')

    if ex.validate_input(category_name, 1, 16, str):
        hasBudget = input('Does this category have a set budget? [Y/n]\n')

        if hasBudget.lower() == 'y':
            category_budget = input('Budget for ' + category_name + ': ')

            try:
                category_budget = float(category_budget)
                categories_list.append({'category_name': category_name,
                                        'category_budget': category_budget})

                repeat = input('Enter another expense category? [Y/n]\n')

                if repeat.lower() == 'y':
                    get_categories(categories_list)

            except (Exception):
                print('Invalid input! That\'s not a valid number!')
                get_categories(categories_list)

        else:
            categories_list.append({'category_name': category_name,
                                    'category_budget': None})

            repeat = input('Enter another expense category? [Y/n]\n')

            if repeat.lower() == 'y':
                get_categories(categories_list)

    else:
        print('Invalid input! Your category name is too big or too small!')
        get_categories(categories_list)

    return categories_list


def get_monthly_budget(budget_var):
    """
    Recursively get the monthly budget from the user and return it in an array.
    """
    monthly_budget = input('Enter monthly budget: ')

    if ex.validate_input(monthly_budget, 1, 18, str):
        try:
            monthly_budget = float(monthly_budget)
            budget_var.append(monthly_budget)

        except (Exception):
            print('Invalid number, please try again!')
            get_monthly_budget(budget_var)
    else:
        print('Invalid number, please try again!')
        get_monthly_budget(budget_var)

    return budget_var


def display_options():
    """
    Display all possible options to the user, allow them to choose their desired option and then direct program flow towards that desired option. For instance, if option 1 is selected, a method to allow the user to enter monthly income will be called.
    """

    options = ['1. Enter monthly income', '2. Set monthly budget', '3. Enter expense', '4. Add expense category', '5. View expense report for day',
               '6. View expense report for week', '7. View expense report for year', '8. View expense report for category', '9. Export expense report', '10. Exit']

    for option in options:
        print(option)

    option_choice = get_user_option([])

    if option_choice[0] == 1:
        get_income()

    elif option_choice[0] == 2:
        monthly_budget = get_monthly_budget([])
        sql.store_monthly_budget(monthly_budget[0])

    elif option_choice[0] == 3:
        expense = get_expense()

    elif option_choice[0] == 4:
        categories = get_categories([])
        sql.store_categories(categories)

    elif option_choice[0] == 5:
        pass

    elif option_choice[0] == 6:
        pass

    elif option_choice[0] == 7:
        pass

    elif option_choice[0] == 8:
        pass

    elif option_choice[0] == 9:
        pass

    elif option_choice[0] == 10:
        sys.exit()

    display_options()


def get_user_option(option_var):
    option = input('Choose an option: ')

    try:
        option = int(option)

        if option in range(1, 11):
            option_var.append(option)

        else:
            print('Invalid option! Please enter the number that corresponds with the desired option from the list.')
            get_user_option(option_var)

    except (Exception):
        print('Invalid option! Please enter the number that corresponds with the desired option from the list.')
        get_user_option(option_var)

    return option_var


def get_category_choice(choice_var):
    categories = sql.get_categories()
    category_number = len(categories)
    index = 1

    if category_number > 0:
        for category in categories:
            print(str(index) + '. ' + category)
            index += 1

        category_choice = input('Choose an expense category: ')

        if ex.validate_input(category_choice, 1, 18, str):
            try:
                category_choice = int(category_choice)

                if category_choice in range(1, category_number + 1):
                    choice_var.append(category_choice)
                else:
                    print('Invalid category choice! Please enter a valid category!\n')
                    get_category_choice(choice_var)

            except (Exception):
                print('Invalid category choice! Please enter a valid category!\n')
                get_category_choice(choice_var)
        else:
            print('Invalid category choice! Please enter a valid category!\n')
            get_category_choice(choice_var)
    else:
        print('There are currently no expense categories! Please add some before adding your first expenses.\n')

    return choice_var


def get_expense_date(date_arr):
    print('Date format should be YYYY-MM-DD. Leave blank for the current day. ')
    date = input('Enter expense date: ')

    if ex.validate_date(date):
        date_arr.append(date)
    else:
        print('Incorrect date! Please ensure format is correct!')
        get_expense_date(date_arr)

    return date_arr


def get_expense_amount(amount_arr):
    amount = input('Enter expense amount: ')

    if ex.validate_input(amount, 1, 12, str):
        try:
            amount = float(amount)
            amount_arr.append(amount)
        except (Exception):
            print('Invalid amount! Please enter a valid number!\n')
            get_expense_amount(amount_arr)
    else:
        print('Invalid amount! Please enter a valid number!\n')
        get_expense_amount(amount_arr)

    return amount_arr


def get_expense():
    expense_category = get_category_choice([])
    expense_date = get_expense_date([])
    expense_amount = get_expense_amount([])

    if (expense_category and expense_date) and expense_amount:
        expense = {'category': expense_category[0],
                   'date': expense_date[0], 'amount': expense_amount[0]}

        return expense
