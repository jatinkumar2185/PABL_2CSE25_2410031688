# Experiment 27: Median of an Array (In-Class)

print("Experiment 27: Median of an Array")

arr = [90, 100, 78, 89, 67]
arr.sort()
n = len(arr)

if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n//2 - 1] + arr[n//2]) / 2

print("Output:", median)
