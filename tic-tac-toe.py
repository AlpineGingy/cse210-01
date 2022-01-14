""" 
This code is designed to be a game of tic-tac-toe, the 
users willnumber to enter in as X or O on their turn.

This code was designed to complete an assignment for
CSE 210 week 2

Author: Andruw Sorensen
"""

import random    


def main():

    flip_a_coin()
    
    board = make_board()
    player = "x"

    while not (has_winner(board) or has_draw(board)):
        show_board(board)
        user_choice(board, player)
        player = next_player(player)
    print("Good Game! Thanks for playing!")

def user_choice(board, player):
    choice = input(f"{player.upper()}'s turn - Choose a square (1-9): ")
    choice = int(choice)
    board[choice-1] = player.upper()

def next_player(player):
    if player == "x":
        player = "o"
    else:
        player = "x"
    return player

def make_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def show_board(board):
    print(f"\n{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}\n")

def flip_a_coin():
    coin = None
    heads_or_tails = input("Heads or tails? ")
    decision = random.randint(1, 2)
    if decision == 1:
        coin = "heads"
    else:
        coin = "tails"
    if heads_or_tails.lower() == coin:
        print(f"It was {coin}, you are X's and will go first.")
    else:
        print(f"It was {coin}, you are O's and will go second.")

def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def has_draw(board):
    for square in range(9):
    if board[square] != "x" and board[square] != "o":
        return False
    return True 

main()
