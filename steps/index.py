# Solution 1
# def steps(n):
#     for row_index in range(n):
#         stair = ''
#         for column_index in range(n):
#             if column_index > row_index: 
#                 stair += ''
#             else:
#                 stair += '#'
#         print(stair)
    
# Solution 2
def steps(n, row = 0, stair = ''):
    if n == row:
        return
    
    if n == len(stair):
        print(stair)
        return steps(n, row + 1)

    add = '#' if len(stair) <= row else ' '
    steps(n, row, stair + add)

steps(4)