#bubble sort optimization
#max number of comparition of unoptimized bubble sort and optimized bubble sort
def insertion_sort(m):
    length = len(m)
    for i in range(1, length):
        element = m[i]
        position = i - 1
        while position >= 0 and m[position] > element:
            m[position + 1] , m[position] = m[position] , m[position + 1]
            position -= 1
    return m 
mylist = list(map(int, input("Enter the list elements: ").strip().split()))
print(insertion_sort(mylist))



