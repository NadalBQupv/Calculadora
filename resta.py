
def resta(text):
    numbers = _split(text)
    res = _resta(numbers)
    return res


def _split(text):
    res = []
    elements = text.split()
    for element in elements:
        if element.isdigit():
            res.append(float(element))
    return res


def _resta(numbers):
    s = numbers[0]
    for num in numbers[1:]:
        s -= float(num)
    return s
