def bubble_sort(mylist):
    for i in range(len(mylist)-1):
        sorting = True
        for j in range(i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j] , mylist[j+1] = mylist[j+1] , mylist[j]
                sorting = False
        if sorting:
            break
mylist = list(map(int, input("Enter the array elements: ").strip().split()))
bubble_sort(mylist)