def min_cost_to_buy_apples(C, test_cases):
    results = []

    for i in range(C):
        N, K = test_cases[i][0]
        prices = test_cases[i][1]
        
        # Initialize the dp array with None
        dp = [None] * (K + 1)
        dp[0] = 0  # No cost to buy 0 kg of apples

        for j in range(1, K + 1):
            if prices[j - 1] != -1:  # Only consider available packets
                for k in range(j, K + 1):
                    if dp[k - j] is not None:
                        if dp[k] is None:
                            dp[k] = dp[k - j] + prices[j - 1]
                        else:
                            dp[k] = min(dp[k], dp[k - j] + prices[j - 1])

        result = dp[K] if dp[K] is not None else -1
        results.append(result)

    return results

# Reading input
C = int(input())
test_cases = []

for _ in range(C):
    N, K = map(int, input().split())
    prices = list(map(int, input().split()))
    test_cases.append(((N, K), prices))

# Getting results
results = min_cost_to_buy_apples(C, test_cases)

# Printing results
for result in results:
    print(result)