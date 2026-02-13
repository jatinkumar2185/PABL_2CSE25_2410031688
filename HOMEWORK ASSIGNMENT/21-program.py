# Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

def trap_water(arr):
    n = len(arr)

    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    # fill left max
    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])

    # fill right max
    right_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])

    # calculate water
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - arr[i]

    return water


# input
arr = list(map(int, input("Enter block heights: ").split()))
print(trap_water(arr))
