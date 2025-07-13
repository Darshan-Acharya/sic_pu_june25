#bubble sort optimization
#max number of comparition of unoptimized bubble sort and optimized bubble sort
def insertion_sort(mylist):
    length = len(mylist)
    for i in range(1, length):
        element = mylist [length]
        position = i - 1
        while position >= 0 and mylist[position] > elements:
            mylist[position + 1] = mylist[position]
    return mylist 
mylist = list(map(int, input().strip().split()))
insertion_sort(mylist)



