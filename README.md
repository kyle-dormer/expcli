# ExpCli
An expense management tool for the command-line. Using it, you can track your
expenses across days, weeks, months and even years - without ever leaving the
terminal.

## Outline
1. Write a report including the design and specification of your project, along with the techniques used for implementation (30%).
2. Develop the product (software) using appropriate programming concepts and conventions (50%).
3. Develop a testing process (10%).
4. Demonstrate a working prototype of your software with all the features you've developed (10%).

## Problem Description
* Our daily routine involves several different financial transactions, from daily groceries to clothing, monthly rent and other expenses. It is quite easy to lose track of your expenses, however, an expense management software can help us track and manage our budget.
* You are required to develop an interactive command line Expense Management Software that enables the user to track and manage their expenses.


## Features
* The ability to enter monthly income, from a single or multiple sources
* Able to set a monthly budget for specific categories of expense - as well as
  overall
* Able to enter expenses based on categories
* Able to add new categories
* Able to view expense reports (with respect to any duration of time and/or
  category)
* Able to generate expense reports in PDF format or in an Excel data sheet
* Averages expenses in respect to a category/categories
* Gives an average for over/under expense for a specific category in a specific
  month
* Stores data using a backend database in SQLite
* Uses *Pandas* and *Matplotli* for data analysis and visualisation
* Can do an export of data to an MS excel datasheet

## Submit
At least a single electronic report and source code via Moodle with at least the following sections:
1. Introduction - a short informal description of the software, its objectives and an indication of the extent to which it has been implemented and any problems faced in its development.
2. Design of system - Discussion and reflection on the design and development of the software, showing the structure of the software and identifying appropriate features. Discussion of implementation logic, code snippets, diagrams and screenshots where needed.
3. **Testing the system** - A set of test results to be submitted. A discussion on failed tests and how much of your code you think your tests cover. Do they cover every aspect?

* Appendix 1: User Guide
* Appendix 2: Code
* Appendix 3: Test Suites

Submit/add the complete software code for your system, appropriate data and test-cases as a zip file.

## Grades

To achieve a 2:1:
* Project is fully functional, advanced application and complexity.
* Report has good reflection, is coherent and organised, good integration of academic and practical issues, good evaluation of deliverables.
* Well explained demonstration showing prototype and working application.
* Good quality and relevant academic references.

## TODO
- [ ] Analyse software requirements and formalise a requirements document
      according to the waterfall SDLC
- [ ] Research and learn SQLite
- [ ] Design the database (in a normalised format)
- [ ] Design software (including modules and their subsequent flowcharts and
      pseudocode)
- [ ] Implement database in SQLite
