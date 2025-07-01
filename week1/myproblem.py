#AGE CALCULATOR
dob = list(map(int, input("Enter your DOB: ").strip().split()))
cur_day = [17, 6, 2025]
d, m, y = cur_day
d1, m1, y1 = dob
if d-d1<0:
    m-=1
    d+=30
if m-m1<0:
    y-=1
    m+=12
if y-y1<0:
    print("DateOfBirth can't be greater than current date: ")
else:
    print(f'your age is {y-y1} years {m-m1} months and {d-d1} days')
    
    
