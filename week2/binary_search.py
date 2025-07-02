def binary_search(mylist, size, key):

    low = 0
    high = size-1

    while(low <= high):
        mid = (high + low)//2
        
        if mylist[mid] == key:
            return (f"{key} is positioned at {mid} index")
        elif mylist[mid] > key:
            high = mid-1
        else:
            low = mid + 1
        
mylist = list(map(int, input("Enter the array elements: ").strip().split()))
size = len(mylist)
key = int(input("Enter the key element to search: "))
binary_search(mylist, size, key)
