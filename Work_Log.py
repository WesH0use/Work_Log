import datetime
import csv

def search():
    """
    This function provides search options for the user to use on the work log
    """
    while True:
        search_input = input("""Do you want to search by: \n
                             a) Exact Date\n
                             b) Time spent\n
                             c) Exact Search\n
                             d) Pattern\n
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




def search_by_time_spent(user_input):
    """
    Search the csv file for a matching time spent provided by the user.
    """
    try:
        with open("log.csv", newline='') as csvfile:
            fieldnames = ["Date", "Name", "Time", "Notes"]
            log_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            rows = list(log_reader)

            found = False
            for row in rows:
                if row["Time"]==str(user_input):
                    found = True
                    print('Date:', row['Date'])
                    print('Title:', row['Task Name'])
                    print('Time Spent:', row['Time Spent'])
                    print('Notes:', row['Notes'])
                    print('')
            if found:
                input("Search result displayed. Please hit enter to return to the main menu")

            if not found:
                print("Search entry does not exist")

    except FileNotFoundError:
        print("No entries have been recorded yet")
        input("Please press enter to return to the main menu")


def date_search_valid():
    """
    This checks to see if the date provided by the user is valid using datetime.datetime. If it is valid
    it runs it through a search by date function.
    """

    while True:

        search_input = input("Please provide a date using the MM/DD/YYYY format ")

        try:
            datetime.datetime.strptime(search_input, "%m/%d/%Y")
            search_by_date(search_input)
            break

        except ValueError:
            print("Please provide a valid date using the format MM/DD/YYYY")


def search_by_date(search_input):
    """
    Search the csv file for a matching date provided by the user.
    """
    try:
        with open("log.csv", newline='') as csvfile:
            fieldnames = ["Date", "Name", "Time", "Notes"]
            log_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            rows = list(log_reader)

            found = False
            for row in rows:
                if row["Date"] == search_input:
                    found = True
                    print('Date:', row['Date'])
                    print('Title:', row['Task Name'])
                    print('Time Spent:', row['Time Spent'])
                    print('Notes:', row['Notes'])
                    print('')
            if found:
                input("Search result displayed. Please hit enter to return to the main menu")

            if not found:
                print("Search entry does not exist")



def date_add():
    """
    This asks the user for the date of the task. It requires the format to be MM/DD/YYYY.
    """

    while True:
        date_input = input("Please provide a date for the tasking. Use the format MM/DD/YYYY: ")

        try:
            datetime.datetime.strptime(date_input, '%m/%d/%Y')
            return date_input

        except ValueError:
            print("Please provide a valid date")


def add_entry(task_date, task_name, time_spent, notes):
    """
    This function takes variables from user input and writes them out to a CSV file. If no file exists
    one is created. Objects are stored as Dictwriter so that they can be searched later on easily.
    """
    with open('log.csv', 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Name', 'Time Spent', 'Notes']
        log_writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        log_writer.writerow({
            "Date": "{}".format(task_date),
            "Name": "{}".format(task_name),
            "Time": "{}".format(time_spent),
            "Notes": "{}".format(notes)
        })


def main_menu():
    """Display window that prompts user for
    either new entry or search previous entries"""

    while True:
        start_prompt = input("""WORK LOG 
                        \n WHAT WOULD YOU LIKE TO DO? Please select 'a' or 'b'.
                        \n a) Add a new entry
                        \n b)Search in existing entries 
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

            print("Your entry has been added. Please press enter to return to the main menue")

        if start_prompt.lower() == 'b':
            search()
            continue
            # create search function









# ask for task name
# ask how much time was spent on the task
# ask any general notes about the task
# record each of these items into a row of a CSV file along with a date

# User should be promted with a menu to choose whether to add a new entry or lookup previous entries
# User should, if she choses to enter a new work log, be able to provide a task name,  number of minutes spent working on it, and any additional notes
# If user wants to find a previous entry they should be presented with four options: find by date, find by time, find by exact search, find by pattern (more details instructions)

# Users should be able to find all of the tasks that were done on a certain date
# Users should be able to match a search string (regex or plain text search)
# Print a report of this information onto the screen, including date, title of task, time spend and general notes

# check for errors







