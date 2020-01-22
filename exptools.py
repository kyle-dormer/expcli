#!/usr/bin/python3
"""
Author: Kyle Dormer
Date: 27/10/2019
Student Number: s1802423
"""

from datetime import datetime


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
