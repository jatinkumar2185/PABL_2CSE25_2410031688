# Experiment 24: Three Way Partitioning (Take-Home)

print("Experiment 24: Three Way Partitioning")

arr = [1, 4, 3, 6, 2, 1]
a = 1
b = 3

low = []
mid = []
high = []

for num in arr:
    if num < a:
        low.append(num)
    elif a <= num <= b:
        mid.append(num)
    else:
        high.append(num)

result = low + mid + high
print("Output:", result)
