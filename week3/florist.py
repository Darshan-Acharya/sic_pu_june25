def get_minimum_cost(k, c):
    c.sort()(reverse = True)
    i = k
    minimum_cost = 0
    while i > 0:
        




nk = input("Enter the values for N and K: ").split()
n = int(nk[0])
k = int(nk[1])
flowers_price = list(map(int, input("Enter the costs of flowers: ").split().strip()))

print("")