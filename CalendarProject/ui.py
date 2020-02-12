import storage

def print_menu(title, list_of_options, Exit_message):

    # This function will print the menu
    print(title.center(len(max(list_of_options))+5),"\n")
    for index in range(len(list_of_options)):
        print("({})  {}".format(index + 1, list_of_options[index]))
    print("({})  {}".format(0, Exit_message))


def schedule_user_inputs(list_of_options, Message1, Message2):

    print("\n", "--->{}".format(Message1))    
    inputs_list = []
    while True:
        try:
            for each_item in list_of_options:
                user_input = input(each_item)

                if "title" in each_item:
                    if user_input.isalpha():
                        inputs_list.append(user_input)
                        continue
                    else:
                        raise Exception

                if "start time" in each_item:
                    if 8 <= int(user_input) <= 18:
                        inputs_list.append(user_input)
                        continue
                    else:
                        raise Exception

                if "duration" in each_item:
                    if 1 <= user_input <= 2 and 8 <= (inputs_list[1] + user_input) <= 18:
                        inputs_list.append(user_input)
                        continue
                    else:
                        raise Exception

            break
        
        except Exception:
            inputs_list = []
            print("Enter another value")

    print("\n", "--->{}".format(Message2)) 
    print_schedule_day(inputs_list)

    return inputs_list

def cancel_schedule_user_inputs(list_of_options, Message1, Message2):
    print("\n", "--->{}".format(Message1))   
    inputs_list = []
    while True:
        try:
            for each_item in list_of_options:
                user_input = input(each_item)
                if "start time" in each_item:
                    if 8 <= int(user_input) <= 18:
                        inputs_list.append(user_input)
                        continue
                    else:
                        raise Exception
            break

        except Exception:
            inputs_list = []
            print("Enter another value")

    print("\n", "--->{}".format(Message2))      
    print_schedule_day(inputs_list)

    return inputs_list





def print_error_message(Message):
    print("Error: {}".format(Message))


def print_schedule_day(items_of_schedule):
    if len(items_of_schedule) == 3:
        print("\n", "Your schedule for the day : {} - {} {}".format(items_of_schedule[2], int(items_of_schedule[2]) + int(items_of_schedule[1]), items_of_schedule[0]), "\n")
    else:
        print("\n", "Your schedule for the day : (Empty)")


