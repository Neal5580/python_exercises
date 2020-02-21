def reverse(str):  
    # Solution 1
    # list1 = list(str)
    # list1.reverse()
    # print("".join(list1))

    # Solution 2
    list1 = str[::-1]
    print(list1)
    return list1

reverse('abcd')