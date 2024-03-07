from art import logo
import os

board = {
    "1": {"1":" ","2":" ","3":" "},
    "2": {"1":" ","2":" ","3":" "},
    "3": {"1":" ","2":" ","3":" "},
}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_board():
    for row in board:
        print (f"{board[row]['1']} | {board[row]['2']} | {board[row]['3']} ")
        if row != "3":
            print ("---------")

def player_input(player_symbol):
    print(f"It is {player_symbol}'s turn!")
    
    try:
        # Input validation for row
        while True:
            row = input("Row 1, 2 or 3: ")
            if row in board and row.isdigit() and 1 <= int(row) <= 3:
                break
            else:
                print("Invalid input. Please enter a valid row.")

        # Input validation for column
        while True:
            column = input("Column 1, 2 or 3: ")
            if column in board[row] and column.isdigit() and 1 <= int(column) <= 3:
                break
            else:
                print("Invalid input. Please enter a valid column.")

        if board[row][column] == " ":
            update_board(row, column, player_symbol)
        else:
            print("That coordinate is already occupied!")
            player_input(player_symbol)

    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")
        player_input(player_symbol)


        

def update_board(row, column, player_symbol):
    if board[row][column] == " ":
        board[row][column] = player_symbol
        clear_console()
    

def check_winner():
    # Check rows
    for row in board:
        if board[row]['1'] == board[row]['2'] == board[row]['3'] != ' ':
            return True

    # Check columns
    for column in board['1']:
        if board['1'][column] == board['2'][column] == board['3'][column] != ' ':
            return True

    # Check diagonals
    if board['1']['1'] == board['2']['2'] == board['3']['3'] != ' ' or \
       board['1']['3'] == board['2']['2'] == board['3']['1'] != ' ':
        return True

    return False

    

def game(player_x_score, player_o_score):
    player_symbol = "X"

    while True:           
        print(logo)
        display_board()

        print(f"X score: {player_x_score} | O score: {player_o_score}")

        player_input(player_symbol)

        if check_winner():
            print(f"Player {player_symbol} wins!")
            if player_symbol == "X":
                player_x_score += 1
            else:
                player_o_score += 1
            break

        # Check for a tie
        if all(board[row][column] != " " for row in board for column in board[row]):
            print("It's a tie!")
            break

        if player_symbol == "X":
            player_symbol = "O"
        else:
            player_symbol = "X"

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        reset_game()
        game(player_x_score, player_o_score)

def reset_game():
    global board
    board = {
        "1": {"1":" ","2":" ","3":" "},
        "2": {"1":" ","2":" ","3":" "},
        "3": {"1":" ","2":" ","3":" "},
    }
    clear_console()

player_x_score = 0
player_o_score = 0

game(player_x_score, player_o_score)