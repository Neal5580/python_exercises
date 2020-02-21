def maxChar(str):
    charMap = {}
    max = 0
    marChar = ""

    for char in list(str):
        print(char)
        if char in charMap:
            charMap[char] += 1
        else:
            charMap[char] = 1

    print(charMap)

    for char in charMap:
        if charMap[char] > max:
            max = charMap[char]
            marChar = char

    print(marChar)  

    return marChar

maxChar('abcdefghijklmnaaaaa')