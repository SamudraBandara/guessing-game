import random
def play_game(player_name):
    dealer_number = random.randint(0, 10)
    tries=0

    while True:
        guess = int(input(f"{player_name}:" ))
        tries += 1

        if guess < dealer_number:
            print("Try a greater number.")

        elif guess > dealer_number :
            print("Try a smaller number.")

        else :
            print(f"That's right! Number of tries: {tries}")
            return tries

print("Player 1 ,it's your turn !")
player1_tries = play_game("Player1")

print("Player 2,it's your turn!")
player2_tries = play_game("Player2")

if player1_tries < player2_tries :
    print("Winner is player1!")
elif player2_tries < player1_tries :
    print("Winner is player2!")
else :
    print("It is a tie!")