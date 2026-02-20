# Experiment 31: Row with Maximum Number of 1s (Take-Home)

print("Experiment 31: Row with Maximum Number of 1s")

arr = [
    [0,1,1,1],
    [0,0,1,1],
    [1,1,1,1],
    [0,0,0,0]
]

max_count = 0
index = -1

for i in range(len(arr)):
    count = sum(arr[i])
    if count > max_count:
        max_count = count
        index = i

print("Output:", index)
