
def resta(text):
    numbers = text
    if type(text) != list:
        numbers = _split(text)
    
    res = numbers.pop(0)
    while numbers:
        a = numbers.pop(0)
        res -= a
    return res


def _split(text):
    res = []
    elements = text.split()
    for element in elements:
        if element.isdigit():
            res.append(float(element))
    return res


