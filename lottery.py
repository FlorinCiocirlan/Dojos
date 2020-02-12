from random import sample
import time
def generate_random(how_many):
    numbers_list = [str(x) for x in range(1, 81)]
    y = ["10", "16", "49", "58", "76", "73"]
    for i in y:
        numbers_list.remove(i)
    return sample(numbers_list,how_many)

def write_to(what):
    with open("lottery.txt", "w") as file1:
        file1.write(" ".join(what))

def print_result(how_many):
    print("\n".join(generate_random(how_many)))

if __name__ == "__main__":
    while True:
        print_result(10)
        write_to(generate_random(6))
        time.sleep(180)



