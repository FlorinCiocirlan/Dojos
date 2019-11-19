def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        print("Your index is out of list range")
