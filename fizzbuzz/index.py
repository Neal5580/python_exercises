def fizzBuzz(n):
    for index in range(n):
        index += 1
        if index % 3 == 0 and index % 5 == 0:
            print('fizzbuzz')
        elif index % 3 == 0:
            print('fizz')
        elif index % 5 == 0:
            print('buzz')
        else:
            print(index)
    return

fizzBuzz(15)