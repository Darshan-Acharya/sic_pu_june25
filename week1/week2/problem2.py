def missing_elements(arr1, arr2):
    if arr1 > arr2:
        arr1.sort()
        arr2.sort()
        missing_array = []
        for i in range(len(arr2)):
            if arr1[i] == arr2[i]:
                continue
            else:
                missing_array.append(arr1[i])
        set(missing_array)
        print(missing_array)
n = list(map(int, input("Enter the array elements of arr1: ").strip().split()))
m = list(map(int, input("Enter the array elements of arr2: ").strip().split()))
missing_elements(n, m)