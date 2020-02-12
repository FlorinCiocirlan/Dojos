import ui
import storage
import sys
import os

def clear():
    os.system("clear")

def handle_menu():
    options = ["Schedule a new meeting",
               "Cancel an existing meeting"]

    ui.print_menu("Menu", options, "Quit")


def choose_from_menu():
    user_input = input("Choose an action: ")
    if user_input == "1":
        options = ["Enter meeting title: ", "Enter start time: ", "Enter duration in hours (1 or 2): "]
        print("\n")        
        ui.schedule_user_inputs(options, "Schedule a new meeting", "Meeting added.")
    elif user_input == "2":
        options = ["Enter start time: "]
        print("\n")
        ui.cancel_schedule_user_inputs(options, "Cancel an existing meeting", "Meeting canceled.")
    elif user_input == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option")


while True:
    handle_menu()
    try:
        choose_from_menu()
    except KeyError as err:
        ui.print_error_message(err)