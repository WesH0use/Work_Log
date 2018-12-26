import datetime


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

            note = input("Notes (Optional): ")

            # add_entry(task_date, task_name, time_spent, notes)
            # create add_entry function

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







