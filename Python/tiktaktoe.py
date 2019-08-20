from IPython.display import clear_output

board = [' ']*10
game_on = False
announce = ' '
player1_marker = ''
player2_marker = ''


def display_board():
    clear_output()
    global board
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])


def reset_board():
    global board
    board = [' '] * 10


def display_board_with_indexes():
    global board
    board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board()
    reset_board()


def select_marker():
    marker = input("Player 1 select your marker 'X' or 'O'").upper()
    while True:
        if marker == 'X':
            return 'X', 'O'
        elif marker == 'O':
            return 'O', 'X'
        else:
            print('Incorrect selection!')


def start_game():
    global game_on
    start_flag = input("Start the game? Y or N ").upper()
    if start_flag == 'Y':
        game_on = True
    else:
        game_on = False


def play_again():
    global game_on
    restart_flag = input("Play again? Y or N ").upper()
    if restart_flag == 'Y':
        game_on = True
    else:
        game_on = False


def board_full():
    global board
    for i in range(1, 9):
        if board[i] == ' ':
            return False
    else:
        return True


def user_input(marker):
    global board
    player = 'Player 1' if marker == player1_marker else 'Player 2'
    position = int(input(player + ' please enter position:'))
    while True:
        if board[position] == ' ':
            board[position] = marker
            break
        else:
            print('Incorrect position!')


def is_winner(marker):
    global board
    return (board[1] == board[2] == board[3] == marker or
            board[4] == board[5] == board[6] == marker or
            board[7] == board[8] == board[9] == marker or
            board[1] == board[4] == board[7] == marker or
            board[2] == board[5] == board[8] == marker or
            board[3] == board[6] == board[9] == marker or
            board[1] == board[5] == board[9] == marker or
            board[3] == board[5] == board[7] == marker)


def game_play(marker):
    player = 'Player 1' if marker == player1_marker else 'Player 2'
    if board_full():
        print('Match drawn!!')
    else:
        display_board()
        user_input(marker)
        if is_winner(marker):
            display_board()
            print(player + " won. Congratulations!!")
        else:
            marker = player1_marker if marker == player2_marker else player2_marker
            game_play(marker)


print("Welcome to tik-tak-toe! Game follows below indexing:")
display_board_with_indexes()

start_game()

player1_marker, player2_marker = select_marker()
print(player1_marker + ' for Player 1 and ' + player2_marker + ' for Player 2')


while game_on:
    game_play(player1_marker)
    play_again()
    reset_board()

print("Thank you!!")




