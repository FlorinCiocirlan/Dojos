board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
moves = 1
player_2_symbol = "0"
player_1_symbol = "X"
name_player1 = str (input ("What is your name player 1?: ") )
name_player2 = str (input ("What is your name player 2?: ") )
player1wins = False
player2wins = False
def show_board():
    print (board[0], board[1], board[2])
    print (board[3], board[4], board[5])
    print (board[6], board[7], board[8])
show_board()
def player1winscondition():
    if board[0] == board[1] == board[2] == player_1_symbol:
        return True
    elif board[3] == board[4] == board[5] == player_1_symbol:
        return True
    elif board[6] == board[7] == board[8] == player_1_symbol:
        return True
    elif board[0] == board[3] == board[6] == player_1_symbol:
        return True
    elif board[1] == board[4] == board[7] == player_1_symbol:
        return True
    elif board[2] == board[5] == board[8] == player_1_symbol:
        return True
    elif board[0] == board[4] == board[8] == player_1_symbol:
        return True
    elif board[2] == board[4] == board[6] == player_1_symbol:
        return True

def player2winscondition():
    if board[0] == board[1] == board[2] == player_2_symbol:
        return True
    elif board[3] == board[4] == board[5] == player_2_symbol:
        return True
    elif board[6] == board[7] == board[8] == player_2_symbol:
        return True
    elif board[0] == board[3] == board[6] == player_2_symbol:
        return True
    elif board[1] == board[4] == board[7] == player_2_symbol:
        return True
    elif board[2] == board[5] ==board[8] == player_2_symbol:
        return True
    elif board[0] == board[4] == board[8] == player_2_symbol:
        return True
    elif board[2] == board[4] == board[6] == player_2_symbol:
        return True
        

while player1wins != True and player2wins != True and moves < 10:
    try:
        if moves % 2 != 0:
            user_input = input(name_player1 + " , where do you want to put your sign? ")
            if str(user_input) == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" :
                a = int(user_input) - 1
                if board[a] != player_2_symbol:
                    board[a] = player_1_symbol
                    show_board()
                    player1wins = player1winscondition()
                else:
                    moves-=1
                    print("Choose another position")
        else:
            user_input = input(name_player2 + " , where do you want to put your sign? ")
            if str(user_input) == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
                    b = int(user_input)-1
                    if board[b] != player_1_symbol:
                        board[b] = player_2_symbol
                        show_board()
                        player2wins = player2winscondition()
                    else:
                        moves-=1
                        print("Choose another position")
                    
        moves += 1
    except (ValueError, IndexError):
        print("Insert a number between 1 and 9")
        
if player1wins == True:
    print(name_player1 , " won!")
elif player2wins == True:
    print(name_player2 , " won!")
else:
    print("Draw")