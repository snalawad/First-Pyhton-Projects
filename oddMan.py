def findOdd(series):

    dp = [[0 for j in range(27)]
          for i in range(series + 1)]

    for i in range(0, 26):
        dp[1][i] = 1

    for i in range(2, series + 1):
        for j in range(0, 26):

            if (j == 0):
                dp[i][j] = dp[i - 1][j + 1];
            else:
                dp[i][j] = (dp[i - 1][j - 1] +
                            dp[i - 1][j + 1])

    sum = 0
    for i in range(0, 26):
        sum = sum + dp[series][i]

    return sum


series_count = int(input())

series = []

for _ in range(series_count):
    series_item = input()
    series.append(series_item)

result = print(findOdd(series))
