# Experiment 30: Median in Row-wise Sorted Matrix (Take-Home)

print("Experiment 30: Median in Row-wise Sorted Matrix")

matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]

arr = []
for row in matrix:
    arr.extend(row)

arr.sort()
median = arr[len(arr)//2]

print("Output:", median)
