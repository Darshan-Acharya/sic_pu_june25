#Student Score validator for 3 subject entered by the user conse
def score_validator(s):
    valid = 0
    n = len(s)
    total_students = n // 3
    valid_score = []
    for i in range(0, n, 3):
        count = 0
        for j in range(i, i+3):
            if s[j] == 0:
                count += 1
        if count == 0:
            valid += 1
            valid_score.append(s[i:i+3])
    print(f'total students:{total_students}\n valid students: {valid} and their  score: {valid_score}')
scores = list(map(int, input("Enter the list element (size should be multiple of 3):").strip().split()))
score_validator(scores)