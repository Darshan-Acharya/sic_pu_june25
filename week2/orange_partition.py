def orange_partition( position, orange_list):
    orange = orange_list[position]
    for i in range(len(orange_list)):
        if orange_list[i] >= orange:
            orange_list[i] , orange = orange , orange_list[i]
    return orange_list
mylist = list(map(int, input("Enter the Orange size: ").strip().split()))
position = int(input("Enter theselected orange size: "))
orange_partition(position, mylist)