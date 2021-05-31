def convertion(opcion):
    if opcion == 1:
        print("Conversion de Millas a kilometros\n")
        number = float(input("""Ingrese el valor que desea
        convetir\n"""))
        Kilometres = number * 1.609344 
        print(f"El resultado de convertir {number} millas a kilometros es {Kilometres}KM")

    elif opcion == 2:
        print("Conversion Kilometros a Millas\n")
        convert = float(input("Ingres la cantidad que desea convertir\n"))
        millas = convert / 1.609344
        print(f"El resultado de convertir {convert} a kilometros es {millas}")

    else:
        print("Elija una opcion valida")
        presentacion()
        


def presentacion():
    print("Programa para convertir\n Millas a kilometro o kilometros a millas")
    opcion = int(input("""Ingrese la opcion que desee
    1.- Millas a Kilometros
    2.- Kilometros a millas \n"""))
    convertion(opcion)

if __name__ == "__main__":
    presentacion()