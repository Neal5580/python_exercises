def vowels(str):
    checker = ['a', 'e', 'i', 'o', 'u']
    result = 0
    for item in str:
        if item.lower() in checker:
            result += 1
    print(result)
    return

vowels('Hi There!')
vowels('Why do you ask?')