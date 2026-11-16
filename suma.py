
def suma(text):
    numbers = _split(text)
    try:
        numbers[0]
    except:
        raise NotImplementedError
    print(numbers, "Numbers")
    res = 0
    while numbers:
        a = numbers.pop(0)
        res += a
    return res


def _split(text):
    res = []
    elements = text.split()
    for element in elements:
        if element.isdigit():
            res.append(float(element))
    return res


