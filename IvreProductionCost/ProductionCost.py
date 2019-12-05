def enter_number():
    user_input = float(input("Enter price: "))
    return user_input


def calculate_galeria_price():
    final_price = (enter_number() / 1.19) * 0.65
    return final_price


def main():
    while True:
        print(calculate_galeria_price())


main()
