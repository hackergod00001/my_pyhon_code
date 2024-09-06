def solve(X):
    sum = 0
    X1 = X
    X2 = len(str(X))
    while X != 0:
        d = X % 10
        sum = sum + pow(d, X2)
        X = X // 10

    if sum == X1:
        return "YES AMSTRONG"
    else:
        return "NO ARMSTRONG"

T = int(input("Enter the number of test cases: "))
for _ in range(T):
    X = int(input("Enter the number: "))

    out_ = solve(X)
    if out_:
        print(out_)