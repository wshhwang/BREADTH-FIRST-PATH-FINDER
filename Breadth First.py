###
### starts at the tree root and explores all of the neighbor nodes. save it the queue 
### when it is  at the present depth prior to moving on to the nodes at the next depth level.
### Keep running until it run out of the nodes.
### At the end node, it saved in the queue is the path and x_coor made it to keep the record 
### as direction by counting of the x,y position.
###
###

import pygame
import queue


def maze1():
    maze = []
    maze.append(["#","O", "#", "#", "#", "#","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", " ", "#", " ", " ","#"])
    maze.append(["#","#", "#", "#", "X", "#","#"])

    return maze
 

def pathfind(maze, moves):
    for X, end in enumerate(maze[0]): #find X in maze
        if end == "O":
            start = X
    x_coor = start
    y_coor = 0
    for move in moves:
        if move == "L":
            x_coor -= 1
        if move == "R":
            x_coor += 1
        if move == "U":
            y_coor -= 1
        if move == "D":
            y_coor += 1
    
    if maze[y_coor][x_coor] == "X":
        print("Path: " + moves)
        printMaze(maze, moves)
        return True
    return False       


def valid(maze, moves):
    
    for x, end in enumerate(maze[0]):
        if end == "O":
            start = x
    x_coor = start
    y_coor = 0

    for move in moves:
        if move == "L":
            x_coor -= 1
        if move == "R":
            x_coor += 1
        if move == "D":
            y_coor += 1
        if move == "U":
            y_coor -= 1
    
        if not(0 <= x_coor < len(maze[0]) and 0 <= y_coor < len(maze)):
            return False
        elif (maze[y_coor][x_coor] == "#"):
            return False
    return True

def printMaze(maze, path=""):
    for x, end in enumerate(maze[0]):
        if end == "O":
            start = x
    x_coor = start
    y_coor = 0

    end = set()
    for move in path:
        if move == "L":
            x_coor -= 1
        if move == "R":
            x_coor += 1
        if move == "U":
            y_coor -= 1
        if move == "D":
            y_coor += 1
        end.add((y_coor, x_coor))
    
    for y_coor, row in enumerate(maze):
        for x_coor, col in enumerate(row):
            if (y_coor, x_coor) in end:
                print("O ", end="")
            else:
                print(col + " ", end="")
        print()
    return

nums = queue.Queue()
nums.put("")
add = ""
#which maze to find?
maze  = maze1()
print()
print()

while not pathfind(maze, add): 
    #grid = create_grid()
    add = nums.get()
    
    #print(add)
    for y_coor in ["L", "R", "U", "D"]:
        put = add + y_coor
        if valid(maze, put):
            nums.put(put)

print("Breadth First Path Finding")
print()