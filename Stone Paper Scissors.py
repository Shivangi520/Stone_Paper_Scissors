"""WRITE A MENU DRIVEN PROGRAM TO EXECUTE THE GAME OF STONE PAPER SCISSORS BETWEEN THE PLAYER AND COMPUTER. MAKE SURE THE USER'S INPUT IS TAKEN BEFORE
SHOWING THE COMPUTER'S DRAW.THE GAME ENDS AS SOON AS EITHER THE PLAYER OR THE COMPUTER REACHES A TOTAL OF 5 POINT SCORES.

THE RULES ARE AS FOLLOWS:

1. STONE BEATS SCISSORS
2. SCISSORS BEAT PAPER
3. PAPER BEATS THE STONE

IF BOTH HAVE ENTERED SAME CHOICE NO POINT IS AWARDED"""

import random


def game_menu():
    print("Enter 1 for Stone")
    print("Enter 2 for Paper")
    print("Enter 3 for scissors")

user_points=0
computer_points=0
choice= True
while choice:
    print("\nWELCOME TO THE GAME OF STONE PAPER SCISSORS")
    print("Following is a list of options:")
    game_menu()
    ch_u=int(input("Enter your choice:")) #choice of user
    ch_c=random.randint(1,3) #choice of computer
    if (ch_u==1 and ch_c==1) or (ch_u==2 and ch_c==2) or (ch_u==3 and ch_c==3):
        print("\nDraw")
    elif (ch_u==1 and ch_c==3) or (ch_u==2 and ch_c==1) or (ch_u==3 and ch_c==2):
        user_points= user_points+1
        print("\nUser got a point")
    elif (ch_u==1 and ch_c==2) or (ch_u==2 and ch_c==3) or (ch_u==3 and ch_c==1):
        computer_points=computer_points+1
        print("\nComputer got a point")
    else:
        print("Invalid Input")

    if user_points==5:
        print("\nCongratulations!!! YOU WON THE GAME!!!")
        choice=False
    elif computer_points==5:
        print("\nSorry.. You Lost.. Try Again..!")
        choice=False
        
        
