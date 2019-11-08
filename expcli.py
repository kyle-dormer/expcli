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


def get_income_sources(income_sources_list):
    """
    income_sources_list (list) -> list
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
