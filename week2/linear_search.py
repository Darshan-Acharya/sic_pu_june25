#Looping Method
def linear_search(mylist, size, key):
    for i in range(size):
        if mylist[i] == key:
            return f'{key} found at position {i}'
    return f'-1: not found '

#Recursion Method
def linear_search_rec(mylist, size, key):
    if size < 0:
        return -1
    elif mylist[size -1] == key:
        print(f'{key} found at position {size - 1}')
    else:
        return linear_search_rec(mylist, size -1, key)
    return 'Not found'
    
#input Section:
mylist = list(map(int, input("Enter the array elements: ").strip().split()))
size = len(mylist)
key = int(input("Enter the key element to search: "))
print("Linear search using for loop")
linear_search(mylist, size, key)
print("Linear search using for Recursion")
linear_search_rec(mylist, size, key)