import sys

data = sys.stdin.read().rstrip().split("\n")
data = [list(map(int,i.split())) for i in data[:-1]]

dp = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c] is not None:
        return dp[a][b][c]

    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[a][b][c]

for a,b,c in data:
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")