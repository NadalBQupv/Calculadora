from suma import suma
from resta import resta

def _split_resta(text):
    res = text.split("-")
    return res


accion = input("Indica la operación que quieres hacer: ")

comprobante = False
res = 0.0

if "+" in accion and "-" not in accion:
    comprobante = True
    try:
        res = suma(accion)
    except NotImplementedError:
        print("empanao, no puedo sumar eso")
        
elif "-" in accion and "+" not in accion:
    comprobante = True
    res = resta(accion)
elif "-" in accion and "+" in accion:
    comprobante = True
    lista_numeros = _split_resta(accion)
    lista_res = []
    for i in lista_numeros:
        lista_res.append(suma(i))
    res = resta(lista_res)

if comprobante:
    print(res)
