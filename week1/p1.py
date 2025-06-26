#assaignment questions
#1.  Find biggest digit in a number
number = input("Enter a number: ")
big_number = 0
for i in range(1, len(number)):
    for j in range(i):
        big_number = number[j]
        if int(number[i]) > int(big_number):
            big_number = int(number[i])
        else:
            big_number = int(number[j])
    print(big_number)
print(big_number, "is the biggest digit in the Number")