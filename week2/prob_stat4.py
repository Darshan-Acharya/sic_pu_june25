def priority(N, x, y):
    if N >= 2 and x >= 1 and y >= 1 and x + y == N and N <= 2000:
        p_list = []
        my_list = list(map(int, input("Enter the array elements of length N: ").strip().split()))
        if len(my_list) == N:
            my_list.sort()
            p = my_list[y] - my_list[y-1] - 1
            print(p)
            for i in range(p):
                p_list.append(my_list[y-1] + 1)
            print(p_list)
N = int(input("Enter the length of the array"))
x = int(input("Enter the length of xlist: "))
y = int(input("Enter the length of ylist: "))
priority(N, x, y)