# Experiment 29: Search in 2D Matrix (Take-Home)

print("Experiment 29: Search in 2D Matrix")

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

found = False
for row in matrix:
    if target in row:
        found = True

print("Output:", found)
