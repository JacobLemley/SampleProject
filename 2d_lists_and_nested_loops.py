print("=========================================")

number_grid = [
#  C O L U M N
    [1,2,3],    #R
    [4,5,6],    #O
    [7,8,9],    #W
    [0]
]

#number_grid[row][column]
print(number_grid[0][1])
print("--------------------------")
# how to parse through two-dimensional array

for row in number_grid :
    for col in row:
        print(col)


print("=========================================")
