def chunk(items, size):
    chucked = []
    index = 0
    while index < len(items):
        chucked.append(items[index:index + size])
        index = index + size
    print(chucked)
    return
    
# chunk([1, 2, 3, 4], 2)
chunk([1, 2, 3, 4, 5, 6, 7, 8], 3)