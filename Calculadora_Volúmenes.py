
import math

def VolumenCilindro(radio, altura):
    return print(round(math.pi * altura * radio**2,2))


def main():
    print("Programa para calcular diferentes Volumenes")

    opcion = int(input(""" 
        Ingrese que figura quiere saber su volumen
        1.-  Cilindro
        2.-  Esfera
        3.-  Cubo
        4.-  Prisma Rectangular
        5.-  Piramide
        6.-  Cono   
        """))

    if opcion == 1:
        print("Cilindro")
        radio  = float(input("Ingrese el valor del radio del cilindro: "))
        altura = float(input("Ingrese el valor de la altura del cilindro: "))  
        volumen = VolumenCilindro(radio, altura)







if __name__ == "__main__":
    main()