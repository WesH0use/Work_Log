import datetime
import csv
import re

"""
A small program for task management. Users are presented with a main menu giving them the option to add a new entry or 
search through existing entries. Entries have a task name, time spent, date, and optional notes. Searches can be made
through regular expression patterns, dates, string search, and date search. Searches must match exactly. All entries
written to a log.csv file. 
"""


def main_menu():
    """Display window that prompts user for
    either new entry or search previous entries"""

    while True:
        start_prompt = input("""WORK LOG 
                        \n WHAT WOULD YOU LIKE TO DO? Please select 'a' or 'b'.
                        \n a) Add a new entry
                        \n b) Search in existing entries 
    """)
        if start_prompt.lower() == 'a':
            task_date = date_add()
            task_name = input("Name of the task: ")

            while True:
                try:
                    time_spent = int(input("Time spent (rounded in minutes): "))
                    break
                except ValueError:
                    print("Please enter a valid integer")

            notes = input("Notes (Optional): ")

            add_entry(task_date, task_name, time_spent, notes)

            print("Your entry has been added. \n")

        if start_prompt.lower() == 'b':
            search()
            continue


def add_entry(task_date, task_name, time_spent, notes):
    """
    This function takes variables from user input and writes them out to a CSV file. If no file exists
    one is created. Objects are stored as DictWriter so that they can be searched later on easily.
    """
    with open('log.csv', 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Name', 'Time', 'Notes']
        log_writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        log_writer.writerow({
            "Date": "{}".format(task_date),
            "Name": "{}".format(task_name),
            "Time": "{}".format(time_spent),
            "Notes": "{}".format(notes)
        })

def date_add():
    """
    This asks the user for the date of the task. It requires the format to be MM/DD/YYYY.
    """

    while True:
        date_input = input("Please provide a date for the task. Use the format MM/DD/YYYY: ")

        try:
            datetime.datetime.strptime(date_input, '%m/%d/%Y')
            return date_input

        except ValueError:
            print("Please provide a valid date")


def search():
    """
    This function provides search options for the user to use on the work log
    """
    while True:
        search_input = input("""Do you want to search by: \n
                             a) Exact Date\n
                             b) Time spent\n
                             c) Exact Search\n
                             d) Regex Pattern\n
                             e) Return to main menu\n""")

        if search_input.lower() == 'a':
            date_search_valid()

        if search_input.lower() == 'b':
            while True:
                try:
                    user_input = int(input("Please enter time spent (numbers only): "))
                    break
                except ValueError:
                    print("Please enter a valid integer. No decimals or fractions.")

            search_by_time_spent(user_input)

        if search_input.lower() == 'c':
            string_search = input("Please enter your search: ")
            search_by_string(string_search)

        if search_input.lower() == 'd':
            regex_pattern_search = input("Please enter a regex pattern: ")
            user_regex = (re.compile(r'''
                %s
             ''' % regex_pattern_search, re.X | re.M))
            search_by_regex_pattern(user_regex)

        if search_input.lower() == "e":
            break


# a)


def date_search_valid():
    """
    This checks to see if the date provided by the user is valid using datetime.datetime. If it is valid
    it runs it through a search by date function.
    """

    while True:

        date_search_input = input("Please provide a date using the MM/DD/YYYY format ")

        try:
            datetime.datetime.strptime(date_search_input, "%m/%d/%Y")
            search_by_date(date_search_input)
            break

        except ValueError:
            print("Please provide a valid date using the format MM/DD/YYYY")


def search_by_date(date_search_input):
    """
    Search the csv file for a matching date provided by the user.
    """
    try:
        with open("log.csv", newline='') as csvfile:
            fieldnames = ["Date", "Task Name", "Time", "Notes"]
            log_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            rows = list(log_reader)

            found = False
            for row in rows:
                if row["Date"] == date_search_input:
                    found = True
                    print('Date:', row['Date'])
                    print('Title:', row['Task Name'])
                    print('Time:', row['Time'])
                    print('Notes:', row['Notes'])
                    print('')
            if found:
                input("Search result displayed. Please press return to go back to the search option menu \n")

            if not found:
                print("Search entry does not exist")

    except FileNotFoundError:
        print("No entries have been recorded yet")
        input("Please press enter to return to the main menu")


# b)


def search_by_time_spent(user_input):
    """
    Search the csv file for a matching time spent provided by the user.
    """
    try:
        with open("log.csv", newline='') as csvfile:
            fieldnames = ["Date", "Task Name", "Time", "Notes"]
            log_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            rows = list(log_reader)

            found = False
            for row in rows:
                if row["Time"] == str(user_input):
                    found = True
                    print('Date:', row['Date'])
                    print('Title:', row['Task Name'])
                    print('Time:', row['Time'])
                    print('Notes:', row['Notes'])
                    print('')
            if found:
                input("Search result displayed. Please press return to go back to the search option menu")

            if not found:
                print("Search entry does not exist")

    except FileNotFoundError:
        print("No entries have been recorded yet")
        input("Please press enter to return to the main menu")

# c


def search_by_string(string_search):
    """
    Search the csv file for a matching string provided by the user.
    """
    try:
        with open("log.csv", newline='') as csvfile:
            fieldnames = ["Date", "Task Name", "Time", "Notes"]
            log_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            rows = list(log_reader)

            found = False
            for row in rows:
                if row["Task Name"] == string_search or row["Notes"] == string_search:
                    found = True
                    print('Date:', row['Date'])
                    print('Title:', row['Task Name'])
                    print('Time:', row['Time'])
                    print('Notes:', row['Notes'])
                    print('')
            if found:
                input("Search result displayed. Please press return to go back to the search option menu.")

            if not found:
                print("Search entry does not exist")

    except FileNotFoundError:
        print("No entries have been recorded yet")
        input("Please press enter to return to the main menu")


# d


def search_by_regex_pattern(pattern_search):
    """
    Search the csv file for a matching pattern provided by the user.
    """
    try:
        with open("log.csv", newline='') as csvfile:
            fieldnames = ["Date", "Task Name", "Time", "Notes"]
            log_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            rows = list(log_reader)

            found = False
            for row in rows:
                if pattern_search.search(str(row)):
                    found = True
                    print('Date:', row['Date'])
                    print('Title:', row['Task Name'])
                    print('Time:', row['Time'])
                    print('Notes:', row['Notes'])
                    print('')
            if found:
                input("Search result displayed. Please press return to go back to the search option menu.")

            if not found:
                print("Search entry does not exist")

    except FileNotFoundError:
        print("No entries have been recorded yet")
        input("Please press enter to return to the main menu")


main_menu()

