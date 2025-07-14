def selection_sort(my):
    length = len(my)
    count = 0
    for i in range(length -1):
        smallest = i
        for j in range(i+1, length):
            if my[j] < my[smallest]:
                smallest = j
                count += 1

        my[smallest], my[i]  = my[i], my[smallest]
        count += 1
    return my, count
mylist = list(map(int, input("Enter the unsorted list elements: ").strip().split()))
print(selection_sort(mylist))

# import numpy as np
# array1 = np.array([12, 9, 7], [15, 17, 30])