from validaciones import validarNombre, validarTelefono, validarPrecio, validarCategoria, validandoMenu
from metodos import aplicarDescuento

nombre = None
nombreEvento = None
opcion = 0
while opcion != 5:
    print("-"*30)
    print("1. Ingresar cliente")
    print("2. Crear Evento")
    print("3. Aplicar descuento")
    print("4. Mostrar Datos")
    print("5. Salir del programa")
    opcion = int(input("Escoger opcion: "))
    match opcion:
        case 1:
            nombre = input("Ingrese su nombre: ")
            while validarNombre(nombre) == False:
                nombre = input("Ingrese un nombre valido: ")

            telefono = input("Ingrese numero telefono de 8 digitos: ")
            while validarTelefono(telefono) == False:
                telefono = input("Ingrese numero telefono valido de 8 digitos: ")

            correo = input("Ingrese su correo: ")
            while validarNombre(correo) == False:
                correo = input("Ingrese un correo valido: ")
            
            categoria = input("Ingrese si es cliente Nuevo o Antiguo: ")
            aux = categoria[0]
            while validarCategoria(aux.lower()) == True:
                categoria = input("Ingrese una opcion valida: ")
                aux = categoria[0]
            print("-"*30)
            print("Cliente registrado con exito!")

        case 2:
            nombreEvento = input("Ingrese nombre del evento: ")
            while validarNombre(nombreEvento) == False:
                nombreEvento = input("Ingrese nombre del evento valido: ")
            precioInicial = int(input("Ingrese valor del evento: "))
            while validarPrecio(precioInicial) == False:
                precioInicial = int(input("Ingrese valor del evento (debe ser igual o superior a $150,000): "))
        
        case 3:
            precioFinal = aplicarDescuento(precioInicial, aux)
            if precioFinal: 
                print("Se ah aplicado el descuento con exito!")
            else:    
                print("No se pudo aplicar el descuento")
        
        case 4:
            if validandoMenu(nombre, nombreEvento) == False:
                print("Error, registre cliente y evento primero")
                break
            print("--------------------- DATOS CLIENTE Y EVENTO ---------------------")
            print(f"Nombre del cliente: {nombre.capitalize()}")
            print(f"Correo del cliente {correo}")
            print(f"Telefono del cliente: +56 9 {telefono}")
            print(f"Tipo de cliente: Cliente {categoria.capitalize()}")
            print(f"Nombre del evento del Cliente: {nombreEvento.capitalize()}")
            print(f"Precio inicial del evento: ${precioInicial}")
            print(f"Precio final del evento: ${precioFinal}")
            if precioInicial >= 1000000 or aux.lower() == "n":
                print(f"El descuento aplicado fue del 50%")
            else:
                print(f"Precio final del evento: ${precioFinal}")
                print(f"El descuento aplicado fue del 0%")
                

        case 5:
            print("Hasta Luego!")        
        case _:
            print("Ingrese un valor valido")

print("El programa ah finalizado")