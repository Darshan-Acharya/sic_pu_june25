def bubble_sort(mylist):
<<<<<<< HEAD
    n = len(mylist)
    for i in range(n):
        sorting = True
        for j in range(n - i - 1):
=======
    n =len(mylist)
    for i in range(n):
        sorting = True
        for j in range(n-i-1):
>>>>>>> 17592434773c0fbb2cd94921a0f6c94e8dc376b9
            if mylist[j] > mylist[j+1]:
                mylist[j] , mylist[j+1] = mylist[j+1] , mylist[j]
                sorting = False
        if sorting:
            break
    return mylist
<<<<<<< HEAD
mylist = list(map(int, input("Enter the array elements: ").strip().split()))
=======
mylist = list(map(int, input("Enter the array unsorted elements(For bubble_sort): ").strip().split()))
>>>>>>> 17592434773c0fbb2cd94921a0f6c94e8dc376b9
print(bubble_sort(mylist))