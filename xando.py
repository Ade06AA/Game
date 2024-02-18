#!/usr/bin/env python


def board(content=[[1,2,3],[4,5,6],[7,8,9]]):
    mylist = [x for y in content for x in y]
    board = """
                                    NUMBERS AND LOCATIONS
       #      #                        #      #
    {}  #   {}  #  {}                  1  #   2  #  3
       #      #                        #      #
  ###################             ###################
       #      #                        #      #
    {}  #   {}  #  {}                  4  #   5  #  6
       #      #                        #      #
  ####################            ####################
       #      #                        #      #
    {}  #   {}  #  {}                  7  #   8  #  9
       #      #                        #      #
    """.format(*mylist)
    
    print(board)

    
def check(location, table):
    x, y = location
    x = x if x != -1 else 2
    y = y if y != -1 else 2
    val = table[x][y]
    if x == 0:
        if val == table[x + 1][y] and val == table[x + 2][y]:
            return 1
        if y in [0,2]:
            if y == 0:
                if val == table[x - 1][y - 1] and val == table[x - 2][y - 2]:
                    return 1
            if y == 2:
                if val == table[x + 1][y - 1] and val == table[x + 2][y - 2]:
                    return 1
            if val == table[x][y - 1] and val == table[x][y - 2]:
                return 1
        else:
            if val == table[x][y - 1] and val == table[x][y + 1]:
                return 1
    if x == 1:
        if val == table[x + 1][y] and val == table[x - 1][y]:
            return 1
        if y not in [0,2]:
            if val == table[x - 1][y - 1] and val == table[x + 1][y + 1]:
                return 1
            if val == table[x - 1][y + 1] and val == table[x + 1][y - 1]:
                return 1
            if val == table[x][y - 1] and val == table[x][y + 1]:
                return 1
        else:
            if val == table[x][y - 1] and val == table[x][y - 2]:
                return 1
    if x == 2:
        if val == table[x - 1][y] and val == table[x - 2][y]:
            return 1
        if y in [0,2]:
            if y == 2:
                if val == table[x - 1][y - 1] and val == table[x - 2][y - 2]:
                    return 1
            else:
                if val == table[x - 1][y + 1] and val == table[x - 2][y + 2]:
                    return 1
            if val == table[x][y - 1] and val == table[x][y - 2]:
                return 1
        else:
            if val == table[x][y - 1] and val == table[x][y + 1]:
                return 1

    return 0

def locate(num):
    val = [int(num / 3) if num % 3 != 0 else int(num / 3 - 1) ,
    num % 3 - 1]
    return val

def play(player, table):
    print(f"player {player}({'X' if player == 1 else 'O'}) pls choose a position by entering the number:", end=" ")
    for i in range(6):
        ans = input()
        if ans not in [str(a) for a in range(1,10)]:
            print("wrong input, alowed values are 1 to 9")
            print("pls enter a valid digit", end=':')
        else:
            break
        if i == 5:
            print("""



            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            exiting due to too many wrong input")
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            """)
            exit()
    ans = int(ans)

    if ans not in range(1,10):
        print("wrong number, location not available")
        play(player, table)
        return
    location = locate(ans)
    if eval('table[{}][{}]'.format(*location)) != " ":
        print("that position is ocupaid, pls choose another location")
        play(player, table)
        return
    #     table[location[0]][location[1]]
    exec('table[{}][{}] = "X" if player == 1 else "O"'.format(*location))
    return check(location, table)

def gameloop():
    table = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    for i in range(5):
        check = play(1, table)
        board(table)
        if (check):
            print("""
            ********************************************
            player 1 has won
            ********************************************""")
            exit()
   

        check = play(2, table)
        board(table)
        if (check):
            print("""
            ********************************************
            player 2 has won
            ********************************************""")
            exit()

print("      player 1 is X") 
print("      player 2 is 0")

print("To start press enter")
input("")
print("******Game Started*********")
print("the are the numbers and there coresponding location")
board()
gameloop()

