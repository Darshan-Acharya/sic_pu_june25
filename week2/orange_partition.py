def orange_partition( position, orange_list):
    partition = 
    k = 0
    orange = orange_list[position]
    for i in range(len(orange_list)):
        if orange_list[i] > orange_list[-1]:
            orange_list[k] = orange_list[i]
            k += 1
    orange_list[k] = orange_list[-1]
    print(f'{orange_list} is the list')
mylist = list(map(int, input("Enter the Orange's size(accordingly): ").strip().split()))
position = int(input("Enter the selected orange size: "))
orange_partition(position, mylist)
