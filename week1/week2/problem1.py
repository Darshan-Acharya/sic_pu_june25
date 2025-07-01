def check_arrangement(boys, girls):
    arrangement = True
    if len(boys) == len(girls):
        for i in range(1, len(boys)):
            if girls[i] >= boys[i-1] and boys[i] >= girls[i-1]:
                continue
            else:
                arrangement = not arrangement
                break
        if arrangement and ((girls[0] >= boys[0] and girls[-1] >= boys[-1]) or (girls[0] <= boys[0] and girls[-1] <= boys[-1])):
            return "Yes"
        else:
            return "No"
    else:
        print("Enter the same number of heights in the list.....!")


#input 
test_case = int(input("Enter the test case number: "))
output = []
for i in range(test_case):
    girls = list(map(int, input("Enter the heights of the girls:").strip().split()))
    girls.sort()
    boys = list(map(int, input("Enter the heights of the boys:").strip().split()))
    boys.sort()
    result = check_arrangement(boys, girls)
    output.append(result)
    print(result)
print(output)