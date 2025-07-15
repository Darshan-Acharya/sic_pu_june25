def merge_sort(array):
    length = len(array)
    if length  > 1:
        mid = length //2
        left, right = [:mid:], [mid::]
        merge_sort(left)
        merge_sort(right)
        merge_sort_in(array, left, right)
def merge_sort_in(array, left, right):
    index = 0
    while len(left)> 1 and len(right)> 1:
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
array = list(map(int, input("Enter the space separed array elements (unsorted): ").strip(). split ()))
merge_sort(array)
