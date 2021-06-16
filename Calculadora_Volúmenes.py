
import math

def VolumenCilindro(radio, altura):
    return print(round(math.pi * altura * radio**2,2))

def VolumenEsfera(radio):
    return print(round((4/3)*math.pi*radio**3,2))

def VolumenCubo(longitud):
    return print(round(longitud**3))

def VolumenPrisma(largo, ancho, altura):
    return print(round((largo * ancho)*altura))

def main():
    print("Programa para calcular diferentes Volumenes")

    opcion = int(input(""" 
        Ingrese que figura quiere saber su volumen
        1.-  Cilindro
        2.-  Esfera
        3.-  Cubo
        4.-  Prisma Rectangular  
        """))

    if opcion == 1:
        print("Volumen de Cilindro")
        radio  = float(input("Ingrese el valor del radio del cilindro: "))
        altura = float(input("Ingrese el valor de la altura del cilindro: "))  
        volumen = VolumenCilindro(radio, altura)

    elif opcion == 2:
        print("Volumen de Esfera")
        radio = float(input ("Ingrese el valor del radio de la esfera: "))
        volumen = VolumenEsfera(radio)

    elif opcion == 3:
        print("Volumen de Cubo")
        longitud = float(input("Ingrese el valor de un lado del cubo: "))
        volumen = VolumenCubo(longitud)

    elif opcion == 4:
        print("Volumen de prisma rectangular")
        largo  = float(input("Ingrese el  valor  del   largo del prisma: "))
        ancho  = float(input("Ingrese el  valor  del   ancho del prisma: "))
        altura = float(input("Ingrese el  valor de la altura del primas: "))
        volumen = VolumenPrisma(largo, ancho, altura) 


if __name__ == "__main__":
    main()