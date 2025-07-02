def selection_sort(mylist):
    for i in range(1,  len(mylist)):
        element = mylist[i-1]
        position = i-1
        for j in range(i-1, len(mylist)):
            if mylist[j] < element:
                element = mylist[j]
                position = j
                mylist[position], mylist[i - 1] = mylist[i - 1], mylist[position]
    return mylist
mylist = list(map(int, input("Enter the array elements: ").strip().split()))
selection_sort(mylist)
