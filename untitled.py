index_of_year = 5
    index_of_day = 4
    index_of_month = 3

    find_the_latest_date = []

    maximum_year = 0
    maximum_month = 0
    table = data_manager.get_table_from_file("sales/sales.csv")

    id_of_customer = ""
    
    for row in table:
        if int(row[index_of_year]) > maximum_year:
            maximum_year = int(row[index_of_year])
    for row in table:
        if int(row[index_of_year]) == maximum_year:        
            if int(row[index_of_month]) > maximum_month:
                maximum_month = int(row[index_of_month])

    for row in table:
        if maximum_year == int(row[index_of_year]) and maximum_month == int(row[index_of_month]):
            find_the_latest_date.append(row[index_of_day])
    maximum_day = int(max(find_the_latest_date))

    for row in table:
        if int(row[index_of_year]) == maximum_year and int(row[index_of_month]) == maximum_month and int(row[index_of_day]) == maximum_day:
            id_of_customer += row[-1]
    crm_table = data_manager.get_table_from_file("crm/customers.csv")

    index_of_id = 0
    index_of_customer_name = 1
    for row in crm_table:
        if row[index_of_id] == id_of_customer:
            return "".join(row[index_of_customer_name])






index_of_id = 6

    to_compare_list = [0, 0, 0]
    answer_id = None
    for row in table:
        if int(row[index_of_year]) > to_compare_list[0] and int(row[index_of_month]) > to_compare_list[1] and int(row[index_of_day]) > to_compare_list[2]:
            to_compare_list[0] = int(row[index_of_year])
            to_compare_list[1] = int(row[index_of_month])
            to_compare_list[2] = int(row[index_of_day])
            answer_id = row[index_of_id]

    index_of_id = 0
    index_of_customer_name = 1
