def reverse(str):  
    list1 = list(str)
    list1.reverse()
    print(list1)
    print("".join(list1))
    return list1

reverse('abcd')