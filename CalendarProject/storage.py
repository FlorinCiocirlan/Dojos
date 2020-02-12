def get_file_from_table():

    Table = []

    with open("meetings.txt", "r") as File:
    for row in File:
        Table.append(row)

    return Table


def insert_data_to_file(data):

    Table = []

    with open("meetings.txt", "w") as File:
    for row in File:
        Table.append

