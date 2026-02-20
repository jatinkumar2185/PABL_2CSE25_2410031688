# Experiment 23: Smallest Subarray with Sum Greater Than X (In-Class)

print("Experiment 23: Smallest Subarray with Sum Greater Than X")

arr = [1, 4, 45, 6, 0, 19]
x = 51

min_length = len(arr) + 1

for i in range(len(arr)):
    current_sum = 0
    for j in range(i, len(arr)):
        current_sum += arr[j]
        if current_sum > x:
            min_length = min(min_length, j - i + 1)
            break

print("Output:", 0 if min_length == len(arr) + 1 else min_length)
