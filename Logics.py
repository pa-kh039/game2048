import random 

def start_game():
    # initialising a 4x4 empty matrix with all 0s
    matrix=[]
    for i in range(4):
        matrix.append([0]*4)
    return matrix 

def add_new_2(matrix):
    # add 2 randomly at any empty position
    row=random.randint(0,3)
    col=random.randint(0,3)
    #seraching for an empty cell
    while(matrix[row][col] != 0): 
        row=random.randint(0,3)
        col=random.randint(0,3)
    matrix[row][col]=2
