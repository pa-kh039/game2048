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

#finding the current state of the game
#states: won,lost,game-on
def get_current_state(mat):
    cz=0
    # searching if there is any 2048
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return "WON"
    # searching if there is any 0
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return "GAME NOT OVER"
    # searching if any 2 adjacent cells can be combined to yield an empty cell
    for i in range(4):
        for j in range(4):
            try:
                if mat[i+1][j]==mat[i][j] or mat[i][j]==mat[i][j+1]:
                    return "GAME NOT OVER"
            except:
                pass
    return "LOST"

def compress(mat):
    # a new matrix in which all the non-zero numbers are on one side
    changed=False
    new_mat=[[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                if j!=pos:
                    changed=True
                pos+=1
    return new_mat,changed

def merge(mat):
    # combining the adjacent same elements
    changed=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]>0:
                mat[i][j]=2*mat[i][j]
                mat[i][j+1]=0
                changed=True
    return mat,changed

def reverse(mat):
    #it reverses each row of the matrix
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat

def transpose(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

def move_up(mat):
    trans_mat=transpose(mat)
    new_mat,c1=compress(trans_mat)
    new_mat,c2=merge(new_mat)
    new_mat,temp=compress(new_mat)
    new_mat=transpose(new_mat)
    return new_mat, c1 or c2

def move_down(mat):
    trans_mat=transpose(mat)
    reversed_mat=reverse(trans_mat)
    new_mat,c1=compress(reversed_mat)
    new_mat,c2=merge(new_mat)
    new_mat,temp=compress(new_mat)
    new_mat=reverse(new_mat)
    new_mat=transpose(new_mat)
    return new_mat, c1 or c2

def move_left(mat):
    new_mat,c1=compress(mat)
    new_mat,c2=merge(new_mat)
    c=c1 or c2
    new_mat,temp=compress(new_mat)
    return new_mat,c

def move_right(mat):
    new_mat=reverse(mat)
    new_mat,c1=compress(new_mat)
    new_mat,c2=merge(new_mat)
    new_mat,temp=compress(new_mat)
    fin_mat=reverse(new_mat)
    return fin_mat, c1 or c2

# --------------testing-------------- #
# mat=start_game()
# print(mat)
# add_new_2(mat)
# print(mat)
# add_new_2(mat)
# print(mat)
# mat=move_up(mat)
# print(mat)
# mat=move_right(mat)
# print(mat)
# add_new_2(mat)
# print(mat)
# mat=move_down(mat)
# print(mat)
# add_new_2(mat)
# print(mat)
# mat=move_left(mat)
# print(mat)
# mat=move_down(mat)
# print(mat)