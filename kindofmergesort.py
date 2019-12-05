import random

big_list = [random.randint(0, 100) for i in range(100)]
print(big_list)
print("\n" * 5)

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        Left = arr[:mid]
        Right = arr[mid:]

        mergeSort(Left)
        mergeSort(Right)

        l = r = k = 0

        while l < len(Left) and r < len(Right):
            if Left[l] < Right[r]:
                arr[k] = Left[l]
                l += 1
            else:
                arr[k] = Right[r]
                r += 1
            k += 1
        
        while l < len(Left):
            arr[k] = Left[l]
            k += 1
            l += 1
        while r < len(Right):
            arr[k] = Right[r]
            k += 1
            r += 1
        return arr
print(mergeSort(big_list))

