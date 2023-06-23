import  random
def play():
    user = input(" What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if  user == computer:
        return 'It\'s a tie'

    if  is_win(user, computer):
        return 'You Won!'

    if not is_win(user, computer):
        print("You Lost!!\n"
              "Wanna play again?\n")
        play_again = input("'y' for yes or 'n' for no")
        if play_again == 'y':
            play()
        return 'Bye!!'


def  is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')  \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())