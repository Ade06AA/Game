#!/usr/bin/env python


def board(content=[[1,2,3],[4,5,6],[7,8,9]]):
    mylist = [x for y in content for x in y]
    board = """
       #      #
     {} #   {}  #  {}
       #      #
  ###################
       #      #
    {}  #   {}  #  {}
       #      #
  ####################
       #      #
    {}  #   {}  #  {}
       #      #
    """.format(*mylist)
    print(board)

def locate(num):
    val = [int(num / 3) if num % 3 != 0 else int(num / 3 - 1) ,
    num % 3 - 1]
    return val
    
def check(location, table):
    l

def play(player, table):
    print(f"player {player} pls choose a position by entering the number:", end=" ")
    ans = int(input())
    if ans not in range(1,10):
        print("wrong number, location not available")
        play(player, table)
        return
    location = locate(ans)
    if eval('table[{}][{}]'.format(*location)) != " ":
        print("that position is ocupaid, pls choose another location")
        play(player, table)
        return

    exec('table[{}][{}] = "X" if player == 1 else "O"'.format(*location))
    check()

def gameloop():
    table = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    for i in range(5):
        play(1, table)
        board(table)
        play(2, table)
        board(table)

print("      player 1 is X") 
print("      player 2 is 0")

print("To start press enter")
input("")
print("******Game Started*********")
print("the are the numbers and there coresponding location")
board()
gameloop()

