import re

def anagrams(stringA, stringB):


    listA = list(stringA[::-1].lower())
    listA.sort()

    listB = list(stringB[::-1].lower())
    listB.sort()

    print(listA)
    print(listB)

    if len(listA) != len(listB):
        return False

    index = 0
    result = True

    while index < len(listA) and result:
        if listA[index] == listB[index]:
            index += 1
        else:
            result = False
    print(result)
    return result

anagrams('rail safety', 'fairy tales')