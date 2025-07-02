#assaignment questions
#1.  Find biggest digit in a number
number = input("Enter the Number: ")
my_list = []
for i in number:
    num = int(i)
    my_list.append(num)
    my_list.sort()
print("The largest number is : ", my_list[len(my_list)-1])
#Find 2nd smallest digit in a number
number = input("Enter the Number: ")
my_list = []
for i in number:
    num = int(i)
    my_list.append(num)
    my_list.sort()
print("The second smallest number is : ", my_list[1])
#Count number of Prime digits in a number
number = input("Enter the Number: ")
count = 0
for i in number:
    num = int(i)
    if num in [2, 3, 5, 7]:
        count+=1
print(count)
#Print the Prime numbers in decreasing order between m and n (m < n)
m = int(input("Enter the lower range: "))
n = int(input("Enter the Higher range: "))
<<<<<<< HEAD
for i in range(2, n):
    count = 0
    for j in range(2, i):
        if i%j == 0:
            count+=1
    if count==0:
        
=======
prime = []
for i in range(n, m, -1):
    count = 0
    for j in range(2, i):
        if i%j == 0:
            count += 1
    if count == 0:
        prime.append(i)
print(prime)
>>>>>>> 42842343d916e37c943a627a8f9007d9857ffd6d
