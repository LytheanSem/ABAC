def find_pairs(arr):
    n = len(arr)
    pairs_found = False

    pairs = {}

    for i in range(n):
        for j in range(i + 1, n):
            product = arr[i] * arr[j]
            if product in pairs:
                pairs_found = True
                a, b = pairs[product]
                c, d = arr[i], arr[j]
                return f"{a} {b} , {c} {d}"
            pairs[product] = (arr[i], arr[j])

    return "No pair exists"


# Read input sequence of distinct integers
input_sequence = input("Enter sequence of distinct integers: ")
distinct_integers = list(map(int, input_sequence.split()))

# Find and print pairs if they exist
result = find_pairs(distinct_integers)
print(result)
