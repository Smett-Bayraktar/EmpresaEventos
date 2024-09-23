
def validarNombre(nombre):
    validacion = True
    if nombre == "":
        validacion = False
    return validacion

def validarTelefono(telefono):
    validacion = False
    if len(telefono) == 8:
        validacion = True
    return validacion

def validarPrecio(precio):
    validacion = True
    if precio < 149000:
        validacion = False
    return validacion

def validarCategoria(categoria):
    validacion = True
    if categoria != "n" or categoria != "a":
        validacion = False
    return validacion

def validandoMenu(nombreCliente, nombreEvento):
    validacion = True
    if nombreCliente == None and nombreEvento == None:
        validacion = False
    return validacion