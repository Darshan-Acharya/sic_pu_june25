def isSameReflection(word1, word2):
    if len(word1) == len(word2): 
        for i in range(len(word2)):
            if word2 == word1:
                return print("1") 
            word2 = word2[-1] + word2[:-1:]
        if word1 != word2:
            return print("-1") 
    else:
        print("Length should be same..!")

word1 = input("Enter the original Word: ")
word2 = input("Enter the reflected word: ")
isSameReflection(word1, word2)