# Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

def is_subset(a, b):
    for x in b:
        if x not in a:
            return False
    return True


# input
n = int(input("Enter size of array a: "))
a = list(map(int, input("Enter elements of array a: ").split()))

m = int(input("Enter size of array b: "))
b = list(map(int, input("Enter elements of array b: ").split()))

# check
if is_subset(a, b):
    print("b is a subset of a")
else:
    print("b is NOT a subset of a")
