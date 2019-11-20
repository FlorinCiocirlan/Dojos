# This program will ask the user to enter his name
# Also his age
# And will print his name and his age as a clause


# This function ask the player name
# And store it in a variable called name_user_input which we will use it later
# The function returns a string


def ask_name_user():
    name_user_input = None
    while name_user_input is None:
        try:
            name_user_input = input("Please enter your name: ")
        except ValueError as err:
            #MODIFIED THE PRINT TO SHOW ORIGINAL ERROR MESSAGE
            print("You entered invalid value: %s" % err)
        else:
            print("Thanks for your name")
    return name_user_input


# This function ask the player to enter his age
# Then we will use it further in the main
# The function returns an integer


def ask_age_user():
    age_user_input = None
    while age_user_input is None:
        try:
            age_user_input = int(input("Please enter your age: "))
            assert age_user_input > 0
        except (ValueError, AssertionError) as err:
            print("You entered invalid value: %s" % err)
        else:
            print("Thanks for your age")
    return age_user_input


def main():
    print("Hello mister/miss")
    print("\n" * 3)
    print("Your name is %s and you are %d years old" % (ask_name_user(), ask_age_user()))


main()
