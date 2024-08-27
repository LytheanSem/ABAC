def find_min_price(K, prices):
    dp = [float('inf')] * (K + 1)
    dp[0] = 0

    for i in range(1, K + 1):
        for j in range(1, len(prices) + 1):
            if j <= i and prices[j - 1] != -1:
                dp[i] = min(dp[i], dp[i - j] + prices[j - 1])

    return dp[K] if dp[K] != float('inf') else -1

# Read the number of test cases
C = int(input().strip())

# Process each test case
for _ in range(C):
    # Read the number of friends and the target amount of apples
    N, K = map(int, input().strip().split())

    # Read the prices of the apples
    prices = list(map(int, input().strip().split()))

    # Calculate the minimum price
    result = find_min_price(K, prices)

    # Print the result
    print(result)
