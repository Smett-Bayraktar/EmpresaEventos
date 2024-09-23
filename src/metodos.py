

def aplicarDescuento(precio, categoria):
    if precio >= 1000000 or categoria.lower() == "n":
        descuento = precio*.50
        precioFinal = precio - descuento
    else:
        precioFinal = precio
    return precioFinal 