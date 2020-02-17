def reverseInt(n):
    if n >= 0:
        answer = int(str(n)[::-1])
    else:
        answer = -int(str(-n)[::-1])
    print(answer)

    # var = 123 if False else 321
    # print(var)
    return answer

reverseInt(981)
reverseInt(-981)