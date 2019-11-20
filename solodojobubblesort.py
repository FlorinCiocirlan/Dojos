my_list = [5, 9, 0, 3, 7, 5, 4, 2, 11]

def bubble_sort(x):
    for i in range(len(x) - 1):
        for j in range(i - 1):
            if x[j] > x[i]:
                x[j], x[i] = x[i], x[j]
    return x

print(my_list)

print(bubble_sort(my_list))