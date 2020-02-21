def matrix(n):
    results = [[0 for x in range(n)] for y in range(n)] 

    counter = 1
    startColumn = 0
    endColumn = n 
    startRow = 0
    endRow = n

    while startColumn <= endColumn and startRow <= endRow:
        for i in range(startColumn, endColumn):
            results[startRow][i] = counter
            counter += 1
        startRow += 1

        for i in range(startRow, endRow):
            results[i][endColumn -1] = counter
            counter += 1
        endColumn -= 1

        for i in range(endColumn - 1, startColumn, -1):
            results[endRow -1][i] = counter
            counter += 1
        startRow -= 1

        for i in range(endRow - 1, startRow, -1):
            print(i, startColumn)
            results[i][startColumn] = counter
            counter += 1
        startColumn += 1
    
    print(results)
matrix(3)


# for n in range(5):
#     print(n)

# for n in range(2, 5):
#     print(n)

for n in range(5, 0, -1):
    print(n)
