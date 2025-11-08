from colorama import Fore, Style, init
import random
import time


init(autoreset=True)
board = [" "] * 9
def show_board():
    print()
    for i in range(0, 9 , 3):
        print(f"{Fore.YELLOW}{i+1}{Style.RESET_ALL} | {Fore.YELLOW}{i+2}{Style.RESET_ALL}") | {Fore.YELLOW}{i+3}{Style.RESET_ALL}
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        print("-" * 10)
    print()
    
def winner(p):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7)(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a]==board[b]==board[c]==p for a,b,c in wins)
def full():
    return " " not in board

def find_winning_move(p):
    for (a,b,c) in [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7)(2,5,8),
        (0,4,8),(2,4,6)
    ]:
        spots = board[a], board[b], board[c]
        if spots.count(p) == 2 and spots.count(" ") == 1:
            if board[a] == " ": return a
            if board[b] == " ": return b
            if board[c] == " ": return c
    return None

def ai_move():
    print(Fore.CYAN + "\n💻 Computer is Thinking..." + Style.RESET_ALL)
    time.sleep(1)
    
    move = find_winning_move("O")
    if move is not None:
        print(Fore.GREEN + "Computer found a winning move!" + Style.RESET_ALL)
        board[move] = "O"
        return
    
    move = find_winning_move("X")
    if move is not None:
        print(Fore.YELLOW + "Computer blocks your winning move!" + Style.RESET_ALL)
        board[move] = "O"
        return
    
    if board[4] == " ":
        print(Fore.BLUE + "Computer takes the center spot." + Style.RESET_ALL)
        board[move] = "O"
        return
    corners = [i for i in range[0,2,6,8] if board[i] == " "]
    if corners:
        move = random.choice(corners)
        print(Fore.MAGENTA + "Computer picks a corner." + Style.RESET_ALL)
        board[move] = "O"
        return
    
    empty = [i for i, s in enumerate[board] if s == " "]
    if corners:
        move = random.choice(empty)
        print(Fore.LIGHTBLACK_EX + "Computer takes any open spot." + Style.RESET_ALL)
        board[move] = "O"
        return
    
        
        
    
            
        