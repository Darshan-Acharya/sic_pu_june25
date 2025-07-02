def class_arrangement(boys, girls):
    arrangement = True
    if len(boys) == len(girls):
        for i in range(1, len(boys)+1):
            if (boys[i] >= girls[i-1] and boys[-1] >= girls[-1]) or (boys[i] <= girls[i-1] and boys[-1] <= girls[-1]):
                continue
            else:
                arrangement = False
        if arrangement and (girls[0] >= boys[0] and girls[-1] >= boys[-1]) or (boys[0] >= girls[0] and boys[-1] >= girls[-1]):
            return "Yes"
        else:
            return "No"
test_case = int(input("Enter the test case; "))
for i in range(test_case):
    boys = list(map(int, input("Enter the heights of boys: ")))
    girls = list(map(int, input("Enter the heights of girls: ")))
    class_arrangement(boys, girls)