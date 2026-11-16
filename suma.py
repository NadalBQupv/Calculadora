
def suma(text):
    numbers = _split(text)
    res = _suma(numbers)
    return res


def _split(text):
    res = []
    elements = text.split()
    for element in elements:
        if element.isdigit():
            res.append(float(element))
    return res


def _suma(numbers):
    s = 0
    for num in numbers:
        s += float(num)
    return s
