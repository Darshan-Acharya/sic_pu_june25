def bubble_sort(mylist):
    n = len(mylist)
    for i in range(n):
        sorting = True
        for j in range(n - i - 1):
            if mylist[j] > mylist[j+1]:
                mylist[j] , mylist[j+1] = mylist[j+1] , mylist[j]
                sorting = False
        if sorting:
            break
    return mylist
mylist = list(map(int, input("Enter the array elements: ").strip().split()))
print(bubble_sort(mylist))