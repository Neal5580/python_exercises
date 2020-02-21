def palindrome(str):
    list1 = list(str)
    length = len(list1)
    result = all(list1[index] == list1[length - index -1 ] for index in range(length))
    print(result)
    return result

palindrome("1000000001")