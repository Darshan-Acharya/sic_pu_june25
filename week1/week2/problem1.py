def check_arrangement(boys, girls):
    arrangement = True
    for i in range(1, n):
        if girls[i] >= boys[i-1] and boys[i] >= girls[i-1]:
            continue
        else:
            not arrangement
            break
    if arrangement and ((girls[0] >= boys[0] and girls[-1] >= boys[-1]) or (girls[0] <= boys[0] and girls[-1] <= boys[-1])):
        return "Yes"
test_case = int(input("Enter the test case number: "))
for i in range(test_case):
    output = []
    girls = list(map(int, input("Enter the heights of the girls:").strip().split()))
    boys = list(map(int, input("Enter the heights of the boys:").strip().split()))
    girls = girls.sort()
    boys = boys.sort()
    result = check_arrangement(boys, girls)
    output.append(result)
print(output)