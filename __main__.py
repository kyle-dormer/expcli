#!/usr/bin/python3
"""
Author: Kyle Dormer
Date: 27/10/2019
Student Number: s1802423
"""

import atexit

from expcli import exit_handler, main
atexit.register(exit_handler)

if __name__ == '__main__':
    main()
