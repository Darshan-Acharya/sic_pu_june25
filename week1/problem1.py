#trangle 2nd type:
def triangle(n):
    for i in range(n):
        print(" "*(n-i),"*"*(2*i+1))
n = int(input("Enter the number of lines to print Equilateral-Triangle(Pascle's triangle): "))
triangle(n)