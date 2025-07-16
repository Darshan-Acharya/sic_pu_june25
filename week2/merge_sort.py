def merge_sort(array):
    length = len(array)
    if length == 1:
        return array
    elif length == 2:
        if array[0] > array[1]:
            array[0],array[1] = array[1], array[0]
            return array
        else:
            return array
    elif length  > 2:
        mid = length //2
        left, right = array[:mid:], array[mid::]
        left = merge_sort(left)
        right = merge_sort(right)
        merge_sort_in(array, left, right)
        return array
def merge_sort_in(array, left, right):
    index = 0
    while len(left)> 0 and len(right)> 0:
        if left[0]<= right[0]:
            array[index] = left.pop(0)
            index += 1
        else:
            array[index] = right.pop(0)
            index += 1
    while len(left) != 0:
        array[index] = left.pop(0)
        index += 1
    while len(right) != 0:
            array[index] = right.pop(0)
            index += 1
    return array
array = list(map(int, input("Enter the space separed array elements (unsorted): ").strip(). split ()))
print(merge_sort(array))
