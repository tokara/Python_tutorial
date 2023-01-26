matrix = [
    [1,3,4,],
    [2,5,6,],
    [5,4,7,]
]
#matrix[0]...returns inner list...first row.
print(matrix[0][1]) #...RETURNS '3'
matrix[0][1] = 20  #..change '3' to '20'
print(matrix[0][1])

#Using nested loop to reitarete over items in matrix list.
matrix = [
    [1,3,4,],
    [2.5,6,],
    [5,4,7,]
]
for row in matrix:
    for item in row:
        print(item)