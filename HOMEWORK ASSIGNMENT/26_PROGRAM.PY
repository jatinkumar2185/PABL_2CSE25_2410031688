# Experiment 26: Check if All Elements are Palindrome (Take-Home)

print("Experiment 26: Check if All Elements are Palindrome")

arr = [111, 222, 333, 444, 555]

result = all(str(num) == str(num)[::-1] for num in arr)

print("Output:", result)
