# Experiment 25: Minimum Swaps to Bring Elements <= k Together (Take-Home)

print("Experiment 25: Minimum Swaps to Bring Elements <= k Together")

arr = [2, 1, 5, 6, 3]
k = 3

count = sum(1 for num in arr if num <= k)

bad = sum(1 for i in range(count) if arr[i] > k)
ans = bad

for i in range(len(arr) - count):
    if arr[i] > k:
        bad -= 1
    if arr[i + count] > k:
        bad += 1
    ans = min(ans, bad)

print("Output:", ans)
