
def main():
    print("Programa de calcular area de un triangulo ")
    b = float (input("Ingrese el valor de la base "))
    h = float (input("Ingrese el valor de la altura "))

    li = float(input("ingrese el valor del lado izquierdo "))
    ld = float(input("Ingrese el valor del lado derecho "))

    area = (b*h)/2
    print(area)

    if b == li and li == ld:
        print("Es un triangulo Equilatero")
    elif li == ld or li == b:
        print("Es un triangulo isoceles")
    else:
        print("Es un triangulo escaleno")

if __name__ == "__main__":
    main()