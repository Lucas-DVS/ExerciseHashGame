from round import Round

another_round = 1

player1 = (input(f'Entry with the name of Player One, who gonna play with symbol x: '))
player2 = (input(f'Entry with the name of Player Two, who gonna play with symbol o: '))

while another_round != 0:  # Validates if players will want to play again

    rd = Round()

    rd.round(player1, player2)

    another_round = int(input("Press 1 to player another round or 0 to close the game: "))
    print()

    if another_round == 0:
        print('Bye')
