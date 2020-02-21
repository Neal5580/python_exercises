### ANIMAL CRACKERS
def animal_crackers(text):
    list = text.split()
    print(list[0][0] == list[1][0])
    return list[0][0] == list[1][0]

# animal_crackers('Levelheaded Clama')

### THE OTHER SIDE OF SEVEN
def other_side_of_seven(num):
    return 7 - 2*(num-7)

# other_side_of_seven(4)

### OLD MACDONALD
def old_macdonald(name):
    result = name[:3].capitalize() + name[3:].capitalize()
    print(result)
    return result

# old_macdonald('macdonald')

### MASTER YODA
def master_yoda(text):
    result =  ' '.join(text.split()[::-1])
    print(result)
    return result
     
# master_yoda('I am home')

### ALMOST THERE
def almost_there(n):
    result = abs(100-n) <= 10 or abs(200-n) <= 10
    print(result)
    return result
     
# almost_there(211)

### LAUGHTER
def laughter(pattern,text):
    count = 0
    for idx, _ in enumerate(text):
        if pattern == text[idx:idx + len(pattern):]:
            count += 1
    print(count)

# laughter('hah','hahahah')

### PAPER DOLL
def paper_doll(text):
    result = ""
    for char in text:
        result += char * 3
    print(result)
    return result

# paper_doll('Mississippi')

### BLACKJACK
def blackjack(a,b,c):
    print(sum((a,b,c)))
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) > 21 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        'BUST'
    pass

# blackjack(5,6,7)

### SUMMER OF '69'
