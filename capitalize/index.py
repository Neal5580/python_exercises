# Solution 1
# def capitalize(str):
#     words = []
#     for item in str.split(): 
#         firstChar = item[0].upper()
#         # if len(item) > 1:
#         #     words.append(firstChar + item[1::])
#         # else:
#         #     words.append(firstChar)
#         words.append(firstChar + item[1::] if len(item) > 1 else firstChar)
#     p = ' '.join(words)
#     print(p)
#     return

#Solution 2
def capitalize(str):
    words = [str[0].upper()]
    index = 1
    while index < len(str):
        # if str[index - 1] == ' ':
        #     words.append(str[index].upper())
        # else:
        #     words.append(str[index])
        words.append(str[index].upper() if str[index - 1] == ' ' else str[index])   
        index += 1
    p = ''.join(words)
    print(p)
    return

capitalize('a short sentence')