"""
Name of the program  : Program 32
Objective            :Tic tac toe
Created              :Mon 23rd Nov
Author               :Sri Varshini
"""
import validateinput
TTT=[]
def Initialize_Board():
    global TTT
    TTT =['_','_','_','_','_','_','_','_','_']
    
def Display_Board():
    for i in range (9):
        print(TTT[i],'[' ,i+1,'] \t' , end='')
        if (i+1)%3==0:
            print('\n')
        
def Move():
    for i in range (9):
        while True:
            if i%2==0:
                #block=int(input("Player 1 enter  the position you want:"))
                block=validateinput.input_integer("Player 1 enter  the position you want:")
            else:
                #block=int(input("Player 2 enter  the position you want:"))
                block=validateinput.input_integer("Player 2 enter  the position you want:")
            if block>0 and block<10:
                if TTT[block-1]!= '_':
                    print("Please select a unfilled block.")
                else:
                    break
            else:
                print("Plese enter a number between 1 to 9.")
        if i%2==0:
            TTT[block-1]="x"
            Display_Board()
            if check_winner()==1:
                print("PLAYER 1 WON..!CONGRATULATIONS!")
                break
        else:
            TTT[block-1]="o"
            Display_Board()
            if check_winner()==1:
                print("PLAYER 2 WON..!CONGRATULATIONS!!!")
                break
    else:
        print("MATCH DRAW....")
          
        
#possible ways to win  
def check_winner():
    if TTT[0]==TTT[1] and TTT[1]==TTT[2] and TTT[2]=='o':
        return 1
           
    if TTT[3]==TTT[4] and TTT[4]==TTT[5] and TTT[5]=='o':
        return 1
           
    if TTT[6]==TTT[7] and TTT[7]==TTT[8] and TTT[8]=='o':
        return 1
           
    if TTT[0]==TTT[3] and TTT[3]==TTT[6] and TTT[6]=='o':
        return 1
           
    if TTT[1]==TTT[4] and TTT[4]==TTT[7] and TTT[7]=='o':
        return 1
           
    if TTT[2]==TTT[5] and TTT[5]==TTT[8] and TTT[8]=='o':
        return 1
            
    if TTT[0]==TTT[4] and TTT[4]==TTT[8] and TTT[8]=='o':
        return 1
            
    if TTT[2]==TTT[4] and TTT[4]==TTT[6] and TTT[6]=='o':
        return 1
            
    if TTT[0]==TTT[1] and TTT[1]==TTT[2] and TTT[2]=='x':
        return 1
            
    if TTT[3]==TTT[4] and TTT[4]==TTT[5] and TTT[5]=='x':
        return 1
           
    if TTT[6]==TTT[7] and TTT[7]==TTT[8] and TTT[8]=='x':
        return 1
           
    if TTT[0]==TTT[3] and TTT[3]==TTT[6] and TTT[6]=='x':
        return 1
            
    if TTT[1]==TTT[4] and TTT[4]==TTT[7] and TTT[7]=='x':
        return 1
            
    if TTT[2]==TTT[5] and TTT[5]==TTT[8] and TTT[8]=='x':
        return 1
            
    if TTT[0]==TTT[4] and TTT[4]==TTT[8] and TTT[8]=='x':
        return 1
            
    if TTT[2]==TTT[4] and TTT[4]==TTT[6] and TTT[6]=='x':
        return 1
    
    return 0
#to check if the player wants to play again
while True:
    Initialize_Board()
    Display_Board()
    Move()
    check_winner()
    z= input("Do you want to play again? (y/n)")
    if z not in ('Y', 'y'):
        break
print("THANK YOU..!")
       
