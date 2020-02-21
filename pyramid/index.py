import math

# Solution 1
# def pyramid(n):
#     midpoint = math.floor((2 * n - 1) / 2)
#     print(midpoint)
    
#     for row in range(n):
#         level = ''
#         for column in range(2 * n -1):
#             if midpoint - row <= column and midpoint + row >= column:
#                 level += '#'
#             else:
#                 level += ' '
#         print(level)

# Solution 2
def pyramid(n, row = 0, level = ''):
    if row == n:
        return
    
    if len(level) == 2 * n - 1:
        print(level)
        return pyramid(n, row + 1)
    
    midpoint = math.floor((2 * n - 1) / 2)

    add = ''

    if midpoint - row <= len(level) and midpoint + row >= len(level):
        add = '#'
    else:
        add = ' '
    pyramid(n, row, level + add)


pyramid(3)