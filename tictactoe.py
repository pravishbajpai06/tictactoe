# -*- coding: utf-8 -*-
def display_board(board):
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

test_board=['#','X','O','X','O','X','O','X','O','X']

display_board(test_board)

def player_input():
    marker=''
    #KEEP ASKING FOR X AND O
    while not (marker=='X' and marker =='O'):
        marker=input("player1: Choose X or O").upper()
        if marker=='X':
            return('X','O')
        else:
            return('O', 'X')
            

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return( (board[1]==mark and board[2]==mark and board[3]==mark)  
    or(board[4]==mark and board[5]==mark and board[6]==mark) 
    or(board[7]==mark and board[8]==mark and board[9]==mark)
    or(board[1]==mark and board[4]==mark and board[7]==mark) 
    or(board[2]==mark and board[5]==mark and board[8]==mark) 
    or(board[3]==mark and board[6]==mark and board[9]==mark)
    or(board[1]==mark and board[5]==mark and board[9]==mark) 
    or(board[3]==mark and board[5]==mark and board[7]==mark))

import random

def choose_first():
    flip= random.randint(0,1)
    if flip==0:
        return("player1")
    else:
        return("player2")
        
def space_check(board,position):
    return board[position]==' '
def full_boardcheck(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position= int(input("Choose a position(1-9)"))
    return position

def replay():
    choice=input("Play again: Enter y.upper() or n.upper() ")
    return choice=='Y'


print("..............WELCOME TO टिक टैक् टो .............. ")
while True:
    #PLAY THE GAME
    #SET EVRYTHING UP
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+"will go first")
    play_game=input('Ready to play?\n Enter y or n:' )
    if play_game=='y':
        game_on=True
    else:
        game_on=False

    #GAME PLAY
    while game_on:
        if turn=='player1':
            display_board(the_board)
            #choose the position
            position=player_choice(the_board)

        #place the marker at the position
            place_marker(the_board,player1_marker,position)
        #check if won  
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("CONGRACTULATIONS.....Player 1 has won")
                game_on=False
            else:
                if full_boardcheck(the_board):
                    display_board(the_board)
                    print("THE GAME IS A TIE")
                    game_on=False
                else:
                    turn='player2'
        else:
            display_board(the_board)
        #choose the position
            position=player_choice(the_board)

        #place the marker at the position
            place_marker(the_board,player2_marker,position)
        #check if won  
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("CONGRACTULATIONS.....Player 2 has won")
                game_on=False
            else:
                if full_boardcheck(the_board):
                    display_board(the_board)
                    print("THE GAME IS A TIE")
                    game_on=False
                else:
                    turn='player1'
    if not replay():
        break

    





