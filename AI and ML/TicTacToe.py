import random

board = [' '] * 9

# Function to print the board
def print_board():
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def slct():
    player_icon = input("Please Select Your Icon (\"O\" or \"X\"): ").upper()
    while player_icon not in ['O', 'X']:
        player_icon = input("Invalid choice. Please Select Your Icon (\"O\" or \"X\"): ").upper()
    return player_icon

def plmov(player_icon):
    mov = int(input("Enter your Move (1-9): "))
    while board[mov - 1] != ' ':
        mov = int(input("Invalid move. Enter your Move (1-9): "))
    board[mov - 1] = player_icon

def cmpslct(player_icon):
    return 'X' if player_icon == 'O' else 'O'

def cmpmov(computer_icon):
    mov = random.randint(0, 8)
    while board[mov] != ' ':
        mov = random.randint(0, 8)
    board[mov] = computer_icon

def check_winner():
    if (board[0] == board[1] == board[2] != " " or
        board[3] == board[4] == board[5] != " " or
        board[6] == board[7] == board[8] != " " or
        board[0] == board[3] == board[6] != " " or
        board[1] == board[4] == board[7] != " " or
        board[2] == board[5] == board[8] != " " or
        board[0] == board[4] == board[8] != " " or
        board[2] == board[4] == board[6] != " "):
        return True
    return False

def Game():
    print("Welcome to the TIC TAC TOE Game")
    print("==============================")
    
    player_icon = slct()
    computer_icon = cmpslct(player_icon)

    while True:
        print_board()
        plmov(player_icon)
        if check_winner():
            print_board()
            print("You Win")
            break
        if ' ' not in board:
            print_board()
            print("It's a Tie")
            break
        cmpmov(computer_icon)
        if check_winner():
            print_board()
            print("You Lose")
            break
        if ' ' not in board:
            print_board()
            print("It's a Tie")
            break
Game()