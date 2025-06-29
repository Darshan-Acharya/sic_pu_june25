#assaignment questions

#Check if a year is Leap year
def leap_year():
     if (year%4==0 and year%100!=0) or year%400==0:
    	print(year, " is leap year")
year = int(input("Enter the year to check wheater the year is leap year: "))


# Check if a +ve integer is Perfect square:
def square_verify(square_number)
     while square_number>0:
     	number = int(square_number**0.5)
     	if square_number == number**2:
    		print(square_number, "is a perfect square number")
square_number = int(input("Enter the positive number to check wheather it's perfect square number: ")
square_verify(square_number)

                    
#Find smallest of 3 distinct numbers
def smallest(numbers):
    while len(numbers)==3:
        if numbers[0]<numbers[1] and numbers[0]<numbers[2]:
            print(numbers[0], "is less than rest of the numbers")
            break
        elif numbers[1]<numbers[0] and numbers[1]<numbers[2]:
            print(numbers[1], "is less than rest of the numbers")
            break
        else:
            print(numbers[2], "is less than rest of the numbers")
            break
numbers = list(map(int, input().strip().split()))        
smallest(numbers)

#1.  Find biggest digit in a number
number = input("Enter the Number: ")
my_list = []
for i in number:
    num = int(i)
    my_list.append(num)
    my_list.sort()
print("The largest number is : ", my_list[len(my_list)-1])
#2nd method
number = input("Enter the Number: ")
high = 0
for i in number:
    if high < int(i):
        high = int(i)
print("Highest digit is: ",high)

#Find 2nd smallest digit in a number
number = input("Enter the Number: ")
my_list = []
for i in number:
    num = int(i)
    my_list.append(num)
    my_list.sort()
print("The second smallest number is : ", my_list[1])

#2- attempt
number = input("Enter the Number without zero: ")
mylist = []
for i in number:
    mylist.append(int(i))
mylist = set(mylist)  #for de-duplication 
mylist = list(mylist)  #for de-duplication process
mylist.sort()
print(mylist)
print("smallest digit is: ",mylist[1])


#Count number of Prime digits in a number
number = input("Enter the Number: ")
count = 0
for i in number:
    num = int(i)
    if num in [2, 3, 5, 7]:
        count+=1
print(count)


#Print the Prime numbers in decreasing order between m and n (m < n)
def prime_list(m, n):
    prime = []
    if m >= 2:
        for i in range(m, n):
            count = 0
            for j in range(m, i):
                if i%j == 0:
                    count+=1
            if count==0:
                prime.append(i)
        prime.sort(reverse = True)
        print(f"{prime} is the list of prime numbers from {m} to {n}")
m = int(input("Enter the lower range(should be <=2): "))
n = int(input("Enter the Higher range: "))   
prime_list(m, n)
        

#stack implementation using list
def push():
    element = int(input("Enter the element to insert: "))
    mylist.append(element)
def pop():
    if len(mylist) > 0:
        print(f'popped element is {mylist[-1]}')
        mylist.pop(-1)
    else:
        print("Stack is empty..!")
def display():
    if len(mylist) > 0:
        print(mylist)
    else:
        print("Stack is Empty..!")
mylist = []
while True:
    print("Enter 1.Push 2.Pop 3.display 4.exit")
    choice = int(input("Enter your Chice: "))
    match(choice):
        case 1:
            push()
        case 2:
            pop()
        case 3:
            display()
        case 4:
            print("End of the Program...!")
            break
        case _:
            print("Invalid choice: ")
        

#Find sum of the series n - n2/3 + n4/5 - n8/7 .... m terms (1<=n<=4 and 2<=m<=10)
def series():
    if n in range(1, 5) and  m in range(2, 11):
        sign = -1
        Sum = 0
        for i in range(0, m):
            numerator = n**(2)**i
            denominator = 2*i + 1
            sign = -sign
            term = (sign)*numerator / denominator
            Sum += term
        print(Sum,f" is the sum of firs {m} for term {n}") 
    else:
        print("Enter the n and m value within the range: ")
n = int(input("Enter the term(between 1 to 4): "))
m = int(input("Enter the length(between 2 to 10): "))
series()

#Frequency calculator
def element_frequency():
    countlist = []
    for i in range(len(mylist)):
        count = 0
        if mylist[i] not in countlist:
            for j in range(len(mylist)):
                if mylist[i] == mylist[j]:
                    count += 1
            countlist.append(mylist[i])
            print(f'frequency of {mylist[i]} is {count} times')
mylist = list(map(int, input("Enter the list elements for the frequency calculation: ").strip().split()))
element_frequency()

#deduplication
def list_deduplication():
    newlist = []
    for i in range(len(mylist)):
        count = 0
        if mylist[i] not in newlist:
            newlist.append(mylist[i])
    print(f"deduplicated list is {newlist}")
mylist = list(map(int, input("Enter the list elements for the frequency calculation: ").strip().split()))
list_deduplication()


def kaprekar_constant(n):
    steps = 0
    while n != 6174:
        digits = f"{n:04d}"
        asc = int("".join(sorted(digits)))
        dsc = int("".join(sorted(digits, reverse = True)))
        n = dsc - asc
        steps += 1
    if n == 6174:
        print("kaprekar's constant found after ",steps," steps")
number = int(input("Enter a 4 digit number for kaprekar's number validation: "))
kaprekar_constant(number)


#triangle
def triangle(n):
    for i in range(1, n+1):
        print("*"*i)
n = int(input("Enter the number of lines to print Triangle: "))
triangle(n)


#Equilateral-triangle and 
def triangle(n):
    for i in range(n):
        print(" "*(n-1-i), end='')
        print("* "*(i+1))
n = int(input("Enter the number of lines to print Equilateral-Triangle: "))
triangle(n)


#square
def square(n):
    for i in range(1, n+1):
        if i == 1 or i == n:
            print("* "*n)
        else:
            print("*" + " " * (2 * n - 3)+"*")
n = int(input("Enter the number of lines to print Rectangle: "))
square(n)



def x_shape(n):
    if n%2 == 0:
        print("Enter Only Odd numbers..!!!!!:')")
    else:
        for i in range(n):
            for j in range(n):
                if i == j or j == n - 1 - i:
                    print("*",end = "")
                else:
                    print(" ", end = "")
            print()
n = int(input("Enter Only Odd Numbers for Symmerty: "))
x_shape(n)
#x-shape
def x_shape(n):
    if n >= 3 and n%2 == 1:
        mid = n//2
        for i in range(n):
            for j in range(n):
                if i == 0 or  j == 0 or i == n-1 or j == n-1:
                    print("*", end ='')
                elif i == j or i + j == n - 1:
                    if i == mid and j == mid:
                        print("0", end = '')
                    else:
                        print("*", end = '')

                else:
                    print(" ", end = '')
            print()

n = int(input())
x_shape(n)

