# Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.Return true if such a triplet exists, otherwise, return false.

def has_triplet(arr, target):
    arr.sort()
    n = len(arr)

    for i in range(n - 2):
        l = i + 1
        r = n - 1

        while l < r:
            s = arr[i] + arr[l] + arr[r]

            if s == target:
                return True
            elif s < target:
                l += 1
            else:
                r -= 1

    return False


# Example tests
print(has_triplet([1, 4, 45, 6, 10, 8], 13))   # True
print(has_triplet([1, 2, 4, 3, 6, 7], 10))    # True
print(has_triplet([40, 20, 10, 3, 6, 7], 24)) # False
