
def run(player1, player2, winsPlayer1, winsPlayer2):
    if winsPlayer1 == 2:
        print("Wins player 1 won 2 of 3 games")
        return ("Fin del juego")
    if winsPlayer2 == 2:
        print("Wins player 1 won 2 of 3 games")
        return ("Fin del juego")
        
    print("Gana 2 de 3 partidas")
    if player1 == 1 and player2 == 1:
        print("Tie")

    elif player1 == 1 and player2 == 2:
        print("Wins player 2")
        winsPlayer2 += 1
        inicio()
    
    elif player1 == 1 and player2 == 3:
        print("Wins player 1")
        winsPlayer1 += 1
        inicio()

    elif player1 == 2 and player2 == 1:
        print("Wins player 1")
        winsPlayer1 += 1
        inicio()
        
    elif player1 == 2 and player2 == 2:
        print("Tie")

    elif player1 == 2 and player2 == 3:
        print("Wins player 2")
        winsPlayer2 += 1
        inicio()

    elif player1 == 3 and player2 == 1:
        print("Wins player 2")
        winsPlayer2 +=1
        inicio()

    elif player1 == 3 and player2 == 2:
        print("Wins player 1")
        winsPlayer1 += 1
        inicio()
    
    elif player1 == 3 and player2 == 3:
        print("Tie")
        inicio()
    
    else:
        print(""" E R R O R
        Escoja una opcion valida 
        """)
        inicio()

def inicio():
    player1 =int(input("""
    Piedra papel o tijera
    Player 1 Escoja una opcion
    1.- Piedra
    2.- Papel
    3.- Tijera 
    """))
    player2 = int(input("""Player 2 Escoja una opcion
    1.- Piedra
    2.- Papel
    3.- Tijera
    """))
    run(player1,player2)


if __name__ == "__main__":
    winsPlayer1 = 0
    winsPlayer2 = 0
    inicio()
    