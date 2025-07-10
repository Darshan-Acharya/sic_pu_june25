#assaignment questions

#Check if a year is Leap year
def leap_year(year):
    if (year%4==0 and year%100!=0) or year%400==0:
    	print(year, " is leap year")
year = int(input("Enter the year to check for leap year: "))


# Check if a +ve integer is Perfect square:
def square_verify(square_number):
    number = int(square_number**0.5)
    if square_number > 0:
        if square_number == number**2:
    	    print(square_number, "is a perfect square number")
square_number = int(input("Enter the positive number to check for perfect square number: "))


print(year, " is leap year")
year = int(input("Enter the year to check wheater the year is leap year: "))
leap_year(year)

# Check if a +ve integer is Perfect square:
def square_verify(square_number):
    if square_number > 0:
        number = int(square_number**0.5)         
        if square_number == number**2:
            print(square_number, "is a perfect square number")
square_number = int(input("Enter the positive number to check wheather it's perfect square number: "))
#>>>>>>> 42842343d916e37c943a627a8f9007d9857ffd6d
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
numbers = list(map(int, input("Enter 3 distinct number: ").strip().split()))        
smallest(numbers)

#1.  Find biggest digit in a number
number = input("Enter the Number for biggest digit validation: ")
my_list = []
for i in number:
    num = int(i)
    my_list.append(num)
    my_list.sort()
print("The biggest digit is : ", my_list[len(my_list)-1])
#2nd method
number = input("Enter the Number for biggest digit validation: ")
high = 0
for i in number:
    if high < int(i):
        high = int(i)
print("Biggest digit is: ",high)

#Find 2nd smallest digit in a number
number = input("Enter the Number for 2nd-smallest digit validation: ")
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
print("Ths second smallest digit is(after deduplication): ",mylist[1])


#Count number of Prime digits in a number
number = input("Enter the Number to count the No/ of Prime digits Count: ")
count = 0
for i in number:
    num = int(i)
    if num in [2, 3, 5, 7]:
        count+=1
print(count,"is the count of prime digits")


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
print("Enter the term and it's length for the series (N - N^2/3 + N^4/5......M)")
n = int(input("Enter the term(between 1 to 4)(N): "))
m = int(input("Enter the length(between 2 to 10)(M): "))
series()

#Frequency of a element calculator
def element_frequency(mylist):
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
element_frequency(mylist)

#deduplication
def list_deduplication():
    newlist = []
    for i in range(len(mylist)):
        count = 0
        if mylist[i] not in newlist:
            newlist.append(mylist[i])
    print(f"deduplicated list is {newlist}")
mylist = list(map(int, input("Enter the list elements for the deduplication: ").strip().split()))
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
number = int(input("Enter a 4 digit number for kaprekar's number for step count: "))
kaprekar_constant(number)


#triangle
def triangle(n):
    for i in range(1, n+1):
        print("*"*i)
n = int(input("Enter the number of lines to print Right-Triangle: "))
triangle(n)


#Equilateral-triangle and 
def triangle(n):
    for i in range(n):
        print(" "*(n-1-i), end='')
        print("* "*(i+1))
n = int(input("Enter the number of lines to print Equilateral-Triangle(Pascle's triangle): "))
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


#X - Shape
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
#trangle 2nd type:
def triangle(n):
    for i in range(n):
        print("* "*(2*i+1))
n = int(input("Enter the number of lines to print Equilateral-Triangle(Pascle's triangle): "))
triangle(n)



#x-shape with 0 in centre inside a hallow square

#x-shape
#>>>>>>> 42842343d916e37c943a627a8f9007d9857ffd6d
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

n = int(input("Enter the number of lines for the X-shape Printing inside a Hallow Square where center is 0(enter odd only <=3): "))
x_shape(n)

def benzene():
    for i in range(7):
        for j in range(i, 5):
            if (j == 2 and(i == 0 or i== 6)) or ((i == 2 or i == 4) and (j == 0 or j ==4)):
                print("C", end = '')
            elif (i == 1 and j ==1) or (i == 5 and j ==3):
                print("/", end = '')
            elif (i ==1 and j == 3) or (j == 1 or i == 5):
                print("|", end ='')
            elif (i == 3 and (j == 0 or j == 4)):
                print("|", end = '')

            else:
                print(" ", end = '')
        print()
benzene()   
#pascle's triangle
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
number = int(input("Enter the number of lines for pascle's Triangle: "))
pascle(number)