"""
Author: Kyle Dormer
Date: 27/10/2019
Student Number: s1802423
"""

import exptools as ex


def main():
    pass


def get_income():
    income_sources = get_income_sources([])
    monthly_income_total = 0

    for income_source in income_sources:
        monthly_income_total += income_source['source_income']


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
        categories_list.append({'category_name': category_name})
        repeat = input('Enter another expense category? [Y/n]\n')

        if repeat.lower() == 'y':
            get_categories(categories_list)

    else:
        print('Invalid input! Your category name is too big or too small!')
        get_categories(categories_list)

    return categories_list
