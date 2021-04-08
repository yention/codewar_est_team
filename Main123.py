def convertFractions(arr):
    match = False
    attempt = 1
    while not match:
        for idx, fraction in enumerate(arr):
            if attempt % fraction[1] != 0:
                attempt = attempt + 1
                break
            if idx == len(arr) - 1 and attempt % fraction[1] == 0:
                match = True
    for fraction in arr:
        fraction[0] = int(attempt / fraction[1])
        fraction[1] = attempt
    return arr


print(convertFractions([[1, 1], [1, 3], [1, 7]]))
