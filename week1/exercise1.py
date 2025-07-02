def pascle(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    for i in range(n):
        print(" "*(n-1-i), end = '')
        for j in range(i+1):
            print(triangle[i][j], end = ' ')
        print()
n = int(input("Enter the num: "))
pascle(n)