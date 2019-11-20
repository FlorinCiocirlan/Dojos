my_list = [0, 2, 3, 4, 6, 8, 9]

def descending_bubble_sort(x):
    for i in range(len(x) - 1, 0, -1):
        for j in range(i-1):
            if x[j] < x[i]:
                x[j], x[i] = x[i], x[j]
    return x

print(my_list)

print(descending_bubble_sort(my_list))