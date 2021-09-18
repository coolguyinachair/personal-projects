#! python3
"""
tictactoe.py - A simple tic-tac-toe game.
"""

# tic-tac-toe game

import random

BOARD = {1: "top-l", 2: "top-m", 3: "top-r", 4: "mid-l", 5: "mid-m", 6: "mid-r", 7: "bot-l", 8: "bot-m", 9: "bot-r"}

def drawboard(val):
    """
    to display board
    
    val: dict (board values)
    """
    print(" %s | %s | %s " % (val['top-l'], val['top-m'], val['top-r']))
    print("---+---+---")
    print(" %s | %s | %s " % (val['mid-l'], val['mid-m'], val['mid-r']))
    print("---+---+---")
    print(" %s | %s | %s " % (val['bot-l'], val['bot-m'], val['bot-r']))

def checkdone(val, ch):
    """
    check if game has been won
    
    val: dict (board values)
    ch: char (user/bot character)
    
    returns True if game has been won; False otherwise
    """
    
    # check if there is same character in 3 cells in any direction
    if ch == val['top-l'] and ch == val['top-m'] and ch == val['top-r']:
        return True
    elif ch == val['mid-l'] and ch == val['mid-m'] and ch == val['mid-r']:
        return True
    elif ch == val['bot-l'] and ch == val['bot-m'] and ch == val['bot-r']:
        return True
    elif ch == val['top-l'] and ch == val['mid-l'] and ch == val['bot-l']:
        return True
    elif ch == val['top-m'] and ch == val['mid-m'] and ch == val['bot-m']:
        return True
    elif ch == val['top-r'] and ch == val['mid-r'] and ch == val['bot-r']:
        return True
    elif ch == val['top-l'] and ch == val['mid-m'] and ch == val['bot-r']:
        return True
    elif ch == val['bot-l'] and ch == val['mid-m'] and ch == val['top-r']:
        return True
    else:
        return False

def thirdunfilled(val, cell1, cell2, cell3):
    """
    val: dict (board values)
    cell1: string (cell name)
    cell2: string (cell name)
    cell3: string (cell name)
    
    returns empty cell name out of 3 cells
    """
    if val[cell1] == ' ':
        return cell1
    elif val[cell2] == ' ':
        return cell2
    else:
        return cell3

def twofilled(ch, val):
    """
    check if two cells out of three filled in any direction
    
    ch: char (user/bot character)
    val: dict (board values)
    
    returns name of cell is true; None otherwise
    """
    helper = {}
    
    # set 1 if filled with given character 0 other wise
    for k in val:
        if val[k] == ch:
            helper.setdefault(k, 1)
        else:
            helper.setdefault(k, 0)
    
    # if two cells filled and empty cell available in any direction, return empty cell name
    if 2 == helper['top-l'] + helper['top-m'] + helper['top-r'] and ' ' in (val['top-l'], val['top-m'], val['top-r']):
        return thirdunfilled(val, 'top-l', 'top-m', 'top-r')
    elif 2 == helper['mid-l'] + helper['mid-m'] + helper['mid-r'] and ' ' in (val['mid-l'], val['mid-m'], val['mid-r']):
        return thirdunfilled(val, 'mid-l', 'mid-m', 'mid-r')
    elif 2 == helper['bot-l'] + helper['bot-m'] + helper['bot-r'] and ' ' in (val['bot-l'], val['bot-m'], val['bot-r']):
        return thirdunfilled(val, 'bot-l', 'bot-m', 'bot-r')
    elif 2 == helper['top-l'] + helper['mid-l'] + helper['bot-l'] and ' ' in (val['top-l'], val['mid-l'], val['bot-l']):
        return thirdunfilled(val, 'top-l', 'mid-l', 'bot-l')
    elif 2 == helper['top-m'] + helper['mid-m'] + helper['bot-m'] and ' ' in (val['top-m'], val['mid-m'], val['bot-m']):
        return thirdunfilled(val, 'top-m', 'mid-m', 'bot-m')
    elif 2 == helper['top-r'] + helper['mid-r'] + helper['bot-r'] and ' ' in (val['top-r'], val['mid-r'], val['bot-r']):
        return thirdunfilled(val, 'top-r', 'mid-r', 'bot-r')
    elif 2 == helper['top-l'] + helper['mid-m'] + helper['bot-r'] and ' ' in (val['top-l'], val['mid-m'], val['bot-r']):
        return thirdunfilled(val, 'top-l', 'mid-m', 'bot-r')
    elif 2 == helper['bot-l'] + helper['mid-m'] + helper['top-r'] and ' ' in (val['bot-l'], val['mid-m'], val['top-r']):
        return thirdunfilled(val, 'bot-l', 'mid-m', 'top-r')
    
    # otherwise return None
    else:
        return None

def botturn(bc, uc, val):
    """
    bot's turn in hard mode
    
    val: dict (board values)
    uc: char (user character)
    bc: char (bot character)
    """
    win = twofilled(bc, val)
    two = twofilled(uc, val)
    
    # check if bot can win; make move accordingly
    if win != None:
        val[win] = bc
    
    # check if user is about to win; make move accordingly
    elif two != None:
        val[two] = bc
    
    # check if middle cell is empty; make move accordingly
    elif val['mid-m'] == ' ':
        val['mid-m'] = bc
    
    # check if any corner cell is empty; make move accordingly
    elif ' ' in (val['top-l'], val['top-r'], val['bot-l'], val['bot-r']):
        while True:
            ch = random.choice(('top-l', 'top-r', 'bot-l', 'bot-r'))
            if val[ch] == ' ':
                val[ch] = bc
                break
    
    # check if any side cell is empty; make move accordingly
    else:
        while True:
            ch = random.choice(('top-m', 'mid-r', 'mid-l', 'bot-m'))
            if val[ch] == ' ':
                val[ch] = bc
                break
            
    # display board after bot's turn
    drawboard(val)
    print()
    
def botturnstupid(bc, val):
    """
    bot's turn in easy mode
    
    val: dict (board values)
    bc: char (bot character)
    """
    print("Bot's Turn: ")
    
    # until encounters an empty cell
    while True:
        
        # select a cell at random
        choice = BOARD[random.randint(1, 9)]
        
        # make move if cell is empty
        if val[choice] == ' ':
            val[choice] = bc
            break
    
    # display board after bot's turn
    drawboard(val)
    print()

def userturn(uc, val):
    """
    user's turn
    
    val: dict (board values)
    uc: char (user character)
    """
    
    # until user provides a valid move
    while True:
        
        # take move input
        pos = input("Enter the position where you want to put next %s (use cell name): " % uc)
        
        # if cell exists and cell is blank
        if pos in val.keys() and val[pos] == ' ':
            val[pos] = uc
            break    
        
        # otherwise error message
        print("Cannot put a %s there." % uc)
        
    # display board after turn
    drawboard(val)
    print()
        
def playround(val, uc, bc, f, diff):
    """
    play each round
    
    val: dict (board values)
    uc: char (user character)
    bc: char (bot character)
    f: boolean (whose turn)
    """
    # display empty board
    drawboard(val)
    print()
    
    # take turns
    while True:
        
        # if no blank cells
        if ' ' not in val.values():
            print("It's a draw.\n")
            return
        
        # user's turn
        if f:
            userturn(uc, val)
            f = not f
            if checkdone(val, uc):
                print("You have won!\n")
                return
            
        # bot's turn
        else:
            
            # easy bot
            if diff == 'a':
                botturnstupid(bc, val)
                f = not f
                if checkdone(val, bc):
                    print("The bot has won. Better luck next time. :(\n")
                    return
                
            # hard bot
            else:
                botturn(bc, uc, val)
                f = not f
                if checkdone(val, bc):
                    print("The bot has won. Better luck next time. :(\n")
                    return
    
def playgame():
    """
    play multiple rounds
    """
    
    # initial empty board
    newboard = { "top-l": ' ', "top-m": ' ', "top-r": ' ', "mid-l": ' ', "mid-m": ' ', "mid-r": ' ', "bot-l": ' ', "bot-m": ' ', "bot-r": ' '}
    
    # while user wants to play
    flag = True
    while flag:
        print("Welcome to tic-tac-toe game!\n")
        print("Instructions:")
        print("Please remember the names of each cell.\n")
        print("       |       |       ")
        print(" %s | %s | %s " % ('top-l', 'top-m', 'top-r'))
        print("       |       |       ")
        print("-------+-------+-------")
        print("       |       |       ")
        print(" %s | %s | %s " % ('mid-l', 'mid-m', 'mid-r'))
        print("       |       |       ")
        print("-------+-------+-------")
        print("       |       |       ")
        print(" %s | %s | %s " % ('bot-l', 'bot-m', 'bot-r'))
        print("       |       |       ")
        print()
        
        # difficulty
        print("Select difficulty:\na) Easy\nb) Hard")
        c = input()
        while c not in 'abAB':
            print("You have entered an invalid choice. Please try again.")
            print("Select difficulty:\na) Easy\nb) Hard")
            c = input()
            
        # who makes first move
        print("Do you want to make the first move?\na) Yes\nb) No")
        first = input()
        while first not in 'abAB':
            print("You have entered an invalid choice. Please try again.")
            print("Do you want to make the first move?\na) Yes\nb) No")
            first = input()
        
        # game begins
        if first in 'aA':
            playround(newboard.copy(), 'X', 'O', True, c.lower())
        else:
            playround(newboard.copy(), 'O', 'X', False, c.lower())
        
        # does user still want to play
        print("Do you want to play again?\na) Yes\nb) No")
        again = input()
        while again not in 'abAB':
            print("You have entered an invalid choice. Please try again.")
            print("Do you want to play again?\na) Yes\nb) No")
            again = input()
        if again in 'aA':
            flag = True
        else:
            flag = False
    
    # exit message
    print("Thank you for playing!")
    
playgame()
