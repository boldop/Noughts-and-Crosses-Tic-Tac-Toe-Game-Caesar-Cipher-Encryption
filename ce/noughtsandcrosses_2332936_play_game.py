import random
import os.path
import json
random.seed()

def d_b(board):
    # create a program to sketch the board
    print(' ----------')
    print('|',board[0][0],'|',board[0][1],'|',board[0][2],'|')
    print(' ----------')
    print('|',board[1][0],'|',board[1][1],'|',board[1][2],'|')
    print(' ----------')
    print('|',board[2][0],'|',board[2][1],'|',board[2][2],'|')
    print(' -----------')
    pass

def welcome(board):
    # displays the greeting
    # Call d_b to display the board (board)
    print("The Unbeatable Noughts and Crosses game is here to greet you.")
    d_b(board)
    pass

def i_b(board):
    # develop code to set all elements of the board to one space ' '
    for i in range(3):
        for x in range(3):
           board[i][x]=' '
    return board

def g_p_m(board):
    # create a program that will ask the user which cell to place the X in,
    # and return row and col
    print("Your choices are")
    print('1 2 3 \n4 5 6 \n7 8 9')
    choice=int(input("Choose a number "))
    if choice==1:
        row=0
        col=0
    elif choice==2:
        row=0
        col=1
    elif choice==3:
        row=0
        col=2
    elif choice==4:
        row=1
        col=0
    elif choice==5:
        row=1
        col=1
    elif choice==6:
        row=1
        col=2
    elif choice==7:
        row=2
        col=0
    elif choice==8:
        row=2
        col=1
    elif choice==9:
        row=2
        col=2
    while board[row][col]!=' ':
        print("position is already taken.")
        choice=int(input("Enter a number "))
        if choice==1:
            row=0
            col=0
        elif choice==2:
            row=0
            col=1
        elif choice==3:
            row=0
            col=2
        elif choice==4:
            row=1
            col=0
        elif choice==5:
            row=1
            col=1
        elif choice==6:
            row=1
            col=2
        elif choice==7:
            row=2
            col=0
        elif choice==8:
            row=2
            col=1
        elif choice==9:
            row=2
            col=2
    return row, col

def choose_computer_move(board):
    # write code that allow the machine to choose a cell and enter a nought in
    # and return row and col
    list_of_choices=[1,2,3,4,5,6,7,8,9]
    choice=random.choice(list_of_choices)
    if choice==1:
        row=0
        col=0
    elif choice==2:
        row=0
        col=1
    elif choice==3:
        row=0
        col=2
    elif choice==4:
        row=1
        col=0
    elif choice==5:
        row=1
        col=1
    elif choice==6:
        row=1
        col=2
    elif choice==7:
        row=2
        col=0
    elif choice==8:
        row=2
        col=1
    elif choice==9:
        row=2
        col=2
    while board[row][col]!=' ':
        choice=random.choice(list_of_choices)
        if choice==1:
            row=0
            col=0
        elif choice==2:
            row=0
            col=1
        elif choice==3:
            row=0
            col=2
        elif choice==4:
            row=1
            col=0
        elif choice==5:
            row=1
            col=1
        elif choice==6:
            row=1
            col=2
        elif choice==7:
            row=2
            col=0
        elif choice==8:
            row=2
            col=1
        elif choice==9:
            row=2
            col=2
    return row, col


def check_for_win(board, mark):
    # create a program that will determine whether the player or the machine has won
    # return True if someone won, False otherwise
    if board[0][0]==mark and board[0][1]==mark and board[0][2]==mark:
        return True
    elif  board[1][0]==mark and board[1][1]==mark and board[1][2]==mark:
        return True
    elif  board[2][0]==mark and board[2][1]==mark and board[2][2]==mark:
        return True
    elif  board[0][0]==mark and board[1][0]==mark and board[2][0]==mark:
        return True
    elif  board[0][1]==mark and board[1][1]==mark and board[2][1]==mark:
        return True
    elif  board[0][2]==mark and board[1][2]==mark and board[2][2]==mark:
        return True
    elif  board[0][0]==mark and board[1][1]==mark and board[2][2]==mark:
        return True
    elif  board[0][2]==mark and board[1][1]==mark and board[2][0]==mark:
        return True
    return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    for x in range(3):
        for i in range(3):
            if board[x][i]==' ':
                return False
    return True

def play_game(board):
    # create software to play the game.
    # star with a call to the i_b(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    #repeat the loop
    board = i_b(board)
    d_b(board)
    
    while True:
        row, col = g_p_m(board)
        board[row][col] = 'X'
        d_b(board)
        if check_for_win(board, 'X'):
            return 1
        if check_for_draw(board):
            return 0
        
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        d_b(board)
        if check_for_win(board, 'O'):
            return -1
        if check_for_draw(board):
            return 0
    
    


def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    print ("Your choices are as follows")
    print ("1 for Play game, 2 for save score, 3 for display scores, q for quit")
    choice=input("Enter your choice")
    return choice 

def l_s():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    leaders={}
    with open("leaderboard.txt",'r') as f:
        for line in f:
           (key, val) = line.split()
           leaders[key] = val
    return leaders

def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    player_name=input("Enter your name")
    with open("leaderboard.txt",'a') as f:
        f.write(player_name+" "+str(score)+"\n")
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    print("\n\n\t\tLEADERBOARD\n")
    print("\tName\t\tScore")
    print("\t----\t\t-----")
    for name, score in leaders.items():
        print("\t{}\t\t{}".format(name, score))
    pass


