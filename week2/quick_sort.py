def quick_sort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)
def partition(arr, l, h):
    piv = arr[h]
    k = l
    for i in range(l, h):
        if arr[i] < piv:
            arr[i], arr[k] = arr[k], arr[i]
            k+=1
    arr[k], arr[h] = arr[h], arr[k]
    return k
arr = list(map(int, input("Enter the array elements: ").strip().split()))
l = 0
h = len(arr) - 1
print(quick_sort(arr, l, h))