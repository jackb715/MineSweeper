from curses import *
import sys
import math
from MineSweeper import Field

board_sizeX = 9
board_sizeY = 9

#TODO Problem with coordinate translation between board and screen
def draw_board(stdscr, board):
    stdscr.clear()
    i = 0
    while i < board_sizeY*2+1:
        for j in range(board_sizeX*2+1):
            stdscr.addstr(i,j,"-")
        i = i + 2 
    i = 1 #reset i
    row = 0
    col = 0
    cell = " " 
    while i < board_sizeY*2+1:
        j = 0
        col = 0
        while j < board_sizeX*2+1:
            if j%2==0:
                stdscr.addstr(i,j,'|')
            else: 
                if board.matrix[row][col].visible:
                    coord = [row,col]
                    if board.bomb_coordinates.__contains__(coord):
                        cell = "*"
                    else:
                        cell = str(board.matrix[row][col].value)
                else:
                    cell = " " # show nothing if cell isn't yet visible 
                stdscr.addstr(i,j,cell)
                col = col + 1
            j = j + 1
        i = i + 2
        row = row + 1 
def center_title(stdscr, title_string,height):
    string_length = len(title_string)
    print(str(string_length)  + "\n")
    width = stdscr.getmaxyx()[1]
    print(str(width))
    stdscr.addstr(height,(width//2 - string_length//2), title_string)

def start_game(stdscr):
    stdscr.clear()
    board = Field(board_sizeX,board_sizeY,10)
    draw_board(stdscr,board)
    minX = 1
    maxX = board_sizeX*2
    minY = 1
    maxY = board_sizeY*2
    cursorX = 1
    cursorY = 1
    
    stdscr.move(cursorX,cursorY)
    while True:
        k = stdscr.getch()
        if k == ord('k'):
            if cursorY == 1:
                pass
            else:
                cursorY = cursorY - 2
        elif k == ord('j'):
            if cursorY + 2 > board_sizeY*2:
                pass
            else:
                cursorY = cursorY + 2
        elif k == ord('h'):
            if cursorX == 1:
                pass
            else:
                cursorX = cursorX - 2
        elif k == ord('l'):
            if cursorX + 2 > board_sizeX*2:
                pass
            else:
                cursorX = cursorX + 2
        elif k == ord('\n'):
            coordX = math.floor(cursorX/2)
            coordY = math.floor(cursorY/2)
            board.click(coordY,coordX)
            draw_board(stdscr,board)
            stdscr.refresh()
        else:
            pass
        stdscr.move(cursorY,cursorX)

def select_difficutly(stdscr):
    stdscr.clear()
    center_title(stdscr,"MineSweeper Tui", 0)
    
    offset = 2
    for d in ("Start", "Quit"):
        center_title(stdscr, d, offset)
        offset += 1
    stdscr.move(2, 47);
    while(True):
        k=stdscr.getch()
        y,x = getsyx()
        if(k == ord('k')):
            if(y==0):
                pass
            else:
                stdscr.move(y-1,x)
        elif(k == ord('j')):
           if( y > stdscr.getmaxyx()[0]): 
               pass
           else:
               stdscr.move(y+1,x)
        elif(k == ord('\n')):
            if y == 2:
                start_game(stdscr)
            elif y == 3:
                sys.exit(0) 
def main(stdscr):
    use_default_colors()
    select_difficutly(stdscr) 
wrapper(main)
