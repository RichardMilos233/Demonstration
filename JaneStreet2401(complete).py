import numpy as np 
n=17
missing_row=39
missing_column=missing_row-17
board=np.zeros((n,n))
rows_req=np.array([14,24,24,39,43,missing_row,22,23,29,28,34,36,29,26,26,24,20])
columns_req=np.array([13,20,22,28,30,36,35,39,49,39,39,missing_column,23,32,23,17,13])



row_sums=np.sum(board, axis=1)
column_sums=np.sum(board, axis=0)
class step():
    def __init__(self, x, y, size, direction):
        self.x=x
        self.y=y
        self.size=size
        self.direction=direction
    def __str__(self):
        return 'step('+str(self.x)+','+ str(self.y)+','+ str(self.size)+','+ str(self.direction)+')'
    def next(self):
        self.direction+=1
        if self.direction==9:
            self.direction=1
            self.y+=1
            if self.y==n-self.size*3+1:
                self.y=0
                self.x+=1
                if self.x==n-self.size*3+1:
                    self.x=0
                    self.size-=1



def checkf(submatrix, size, direction):
    subsubm1=submatrix[:size, :size]
    sum1=np.sum(subsubm1)
    subsubm2=submatrix[size:size*2, :size]
    sum2=np.sum(subsubm2)
    subsubm3=submatrix[size*2:size*3, :size]
    sum3=np.sum(subsubm3)
    subsubm4=submatrix[:size, size:size*2]
    sum4=np.sum(subsubm4)
    subsubm5=submatrix[size:size*2, size:size*2]
    sum5=np.sum(subsubm5)
    subsubm6=submatrix[size*2:size*3, size:size*2]
    sum6=np.sum(subsubm6)
    subsubm7=submatrix[:size, size*2:size*3]
    sum7=np.sum(subsubm7)
    subsubm8=submatrix[size:size*2, size*2:size*3]
    sum8=np.sum(subsubm8)
    subsubm9=submatrix[size*2:size*3, size*2:size*3]
    sum9=np.sum(subsubm9)
    if direction==1:
        return sum2+sum4+sum5+sum6+sum7==0
    elif direction==2:
        return sum1+sum4+sum5+sum6+sum8==0
    elif direction==3:
        return sum1+sum2+sum5+sum6+sum8==0
    elif direction==4:
        return sum2+sum3+sum4+sum5+sum8==0
    elif direction==5:
        return sum3+sum4+sum5+sum6+sum8==0
    elif direction==6:
        return sum2+sum4+sum5+sum6+sum9==0
    elif direction==7:
        return sum2+sum4+sum5+sum8+sum9==0
    elif direction==8:
        return sum2+sum5+sum6+sum7+sum8==0
    

def printf(matrix, stp, block):
    x=stp.x
    y=stp.y
    size=stp.size
    direction=stp.direction
    if direction==1:
        matrix[x+size:x+size*2, y:y+size]=block#2
        matrix[x:x+size, y+size:y+size*2]=block#4
        matrix[x+size:x+size*2, y+size:y+size*2]=block#5
        matrix[x+size*2:x+size*3, y+size:y+size*2]=block#6
        matrix[x:x+size, y+size*2:y+size*3]=block#7
    elif direction==2:
        matrix[x:x+size, y:y+size]=block#1
        matrix[x:x+size, y+size:y+size*2]=block#4
        matrix[x+size:x+size*2, y+size:y+size*2]=block#5
        matrix[x+size*2:x+size*3, y+size:y+size*2]=block#6
        matrix[x+size:x+size*2, y+size*2:y+size*3]=block#8
    elif direction==3:
        matrix[x:x+size, y:y+size]=block#1
        matrix[x+size:x+size*2, y:y+size]=block#2
        matrix[x+size:x+size*2, y+size:y+size*2]=block#5
        matrix[x+size*2:x+size*3, y+size:y+size*2]=block#6
        matrix[x+size:x+size*2, y+size*2:y+size*3]=block#8
    elif direction==4:
        matrix[x+size:x+size*2, y:y+size]=block#2
        matrix[x+size*2:x+size*3, y:y+size]=block#3
        matrix[x:x+size, y+size:y+size*2]=block#4
        matrix[x+size:x+size*2, y+size:y+size*2]=block#5
        matrix[x+size:x+size*2, y+size*2:y+size*3]=block#8
    elif direction==5:
        matrix[x+size*2:x+size*3, y:y+size]=block#3
        matrix[x:x+size, y+size:y+size*2]=block#4
        matrix[x+size:x+size*2, y+size:y+size*2]=block#5
        matrix[x+size*2:x+size*3, y+size:y+size*2]=block#6
        matrix[x+size:x+size*2, y+size*2:y+size*3]=block#8
    elif direction==6:
        matrix[x+size:x+size*2, y:y+size]=block#2
        matrix[x:x+size, y+size:y+size*2]=block#4
        matrix[x+size:x+size*2, y+size:y+size*2]=block#5
        matrix[x+size*2:x+size*3, y+size:y+size*2]=block#6
        matrix[x+size*2:x+size*3, y+size*2:y+size*3]=block#9
    elif direction==7:
        matrix[x+size:x+size*2, y:y+size]=block#2
        matrix[x:x+size, y+size:y+size*2]=block#4
        matrix[x+size:x+size*2, y+size:y+size*2]=block#5
        matrix[x+size:x+size*2, y+size*2:y+size*3]=block#8
        matrix[x+size*2:x+size*3, y+size*2:y+size*3]=block#9
    elif direction==8:
        matrix[x+size:x+size*2, y:y+size]=block#2
        matrix[x+size:x+size*2, y+size:y+size*2]=block#5
        matrix[x+size*2:x+size*3, y+size:y+size*2]=block#6
        matrix[x:x+size, y+size*2:y+size*3]=block#7
        matrix[x+size:x+size*2, y+size*2:y+size*3]=block#8

def back(matrix, current_step):
    printf(matrix, current_step, np.zeros((current_step.size,current_step.size)))

def putf(matrix, n, current_step):
    x=current_step.x
    y=current_step.y
    size=current_step.size
    direction=current_step.direction
    if size==0:
        return 3
    if x>n-size*3 or y>n-size*3:
        return 1
    else:
        submatrix=matrix[x:x+size*3, y:y+size*3]
        block=np.zeros((size,size))+size
        if checkf(submatrix, size, direction):
            printf(matrix, current_step, block)
            return 0
        else:
            return 2

def row_column_req(n, row_sums, rows_req, column_sums, columns_req):
    for i in range(n):
        if row_sums[i]>rows_req[i] or column_sums[i]>columns_req[i]:
            return False
    return True

def game_req(n, row_sums, rows_req, column_sums, columns_req):
    for i in range(n):
        if row_sums[i]!=rows_req[i] or column_sums[i]!=columns_req[i]:
            return False
    return True

def zero_detector(lst):
    sorted_list=sorted(lst)
    if sorted_list[0]==0:
        return True
    else:
        return False

def area_req(board):
    area_sum=24
    shapes=[[]]*20
    shapes[0]=[board[0,0],board[1,0],board[2,0],board[3,0],board[4,0],board[5,0],board[6,0],
            board[7,0],board[8,0],board[9,0],board[10,0],board[11,0],board[12,0],board[13,0],
            board[14,0],board[15,0],board[16,0],board[0,1],board[1,1],board[15,1],board[16,1],
            board[1,2],board[16,2],board[16,3],board[14,4],board[15,4],board[16,4],board[14,5],board[16,5]]
    
    shapes[1]=[board[2,1],board[3,1],board[4,1],board[5,1],board[6,1],board[7,1],board[8,1],board[9,1],
            board[10,1],board[11,1],board[12,1],board[13,1],board[14,1],board[2,2],board[3,2],board[14,2],board[15,2],
            board[2,3],board[15,3]]
    
    shapes[2]=[board[0,2],board[0,3],board[1,3],board[3,3],board[4,3],
            board[1,4],board[2,4],board[3,4],
            board[1,5],board[2,5],board[3,5],
            board[1,6],board[2,6],board[3,6]]
    
    shapes[3]=[board[4,2],board[5,2],board[5,3],board[6,3],board[6,4],board[7,4],board[5,5],board[6,5]]

    shapes[4]=[board[6,2],board[7,2],board[8,2],board[9,2],board[10,2],board[11,2],board[12,2],
            board[7,3],board[8,3],board[9,3],board[10,3],board[11,3],
            board[8,4],board[9,4],board[10,4],
            board[9,5]]
    
    shapes[5]=[board[13,2],board[12,3],board[13,3],board[14,3],
            board[12,4],board[13,4],board[12,5],board[13,5],board[12,6],board[13,6],board[12,7],board[13,7],
            board[11,6],board[10,7],board[11,7],board[10,8],board[11,8]]
    
    shapes[6]=[board[0,4],board[0,5],board[0,6],board[0,7],board[0,8],board[0,9],
            board[1,7],board[1,8],board[1,9],board[2,7],board[2,9],board[3,9]]
    
    shapes[7]=[board[4,4],board[5,4],board[4,5],board[4,6],board[4,7],board[3,7],board[3,8],board[2,8]]

    shapes[8]=[board[7,5],board[8,5],board[5,6],board[6,6],board[7,6],board[8,6],board[5,7],board[6,7],board[4,8],board[5,8],board[6,8]]

    shapes[9]=[board[11,4],board[10,5],board[11,5],board[9,6],board[10,6],board[7,7],board[8,7],board[9,7],board[7,8],board[5,9],board[6,9],board[7,9]]

    shapes[10]=[board[15,5],board[14,6],board[15,6],board[16,6],
                board[16,7],board[16,8],board[16,9],board[16,10],board[16,11],board[16,12]]
    
    shapes[11]=[board[4,9],board[4,10],board[5,10],board[6,10],board[7,10],board[8,10],board[9,10],board[8,8],board[8,9],board[8,11],board[8,12],board[7,12],board[9,12]]

    shapes[12]=[board[9,8],board[9,9],board[10,9],board[10,10],board[11,10],board[11,11],board[12,11],board[12,12]]

    shapes[13]=[board[14,7],board[12,8],board[13,8],board[14,8],board[11,9],board[12,9],board[12,10],board[13,10]]

    shapes[14]=[board[15,7],board[15,8],board[13,9],board[14,9],board[15,9],board[15,10],board[15,11],board[14,12],board[15,12],board[14,13],board[15,13],board[16,13]]

    shapes[15]=[board[0,10],board[1,10],board[2,10],board[3,10],board[0,11],board[3,11],board[4,11],board[5,11],board[6,11],board[7,11],
                board[0,12],board[2,12],board[3,12],board[4,12],board[5,12],board[6,12],board[0,13],board[2,13],board[0,14],
                board[0,15],board[1,15],board[0,16],board[1,16],board[2,16],board[3,16],board[4,16]]
    
    shapes[16]=[board[1,11],board[2,11],board[1,12],board[1,13],board[1,14],board[2,14],board[3,14],board[3,13],board[4,13],board[5,13],board[5,14],board[6,14]]

    shapes[17]=[board[9,11],board[10,11],board[10,12],board[6,13],board[7,13],board[8,13],board[9,13],board[10,13],board[8,14],board[10,14],board[10,15],board[11,15]]

    shapes[18]=[board[11,12],board[11,13],board[12,13],board[13,11],board[13,12],board[13,13],board[13,14],board[14,10],board[14,11],board[14,14],board[14,15]]

    shapes[19]=[board[4,14],board[7,14],board[9,14],board[11,14],board[12,14],board[15,14],board[16,14],
                board[2,15],board[3,15],board[4,15],board[5,15],board[6,15],board[7,15],board[8,15],board[9,15],board[12,15],board[13,15],board[15,15],board[16,15],
                board[5,16],board[6,16],board[7,16],board[8,16],board[9,16],board[10,16],board[11,16],board[12,16],board[13,16],board[14,16],board[15,16],board[16,16]]
    
    for i in range(20):
        if sum(shapes[i])>area_sum:
            return False
    return True

def game_req_2(board):
    area_sum=24
    shapes=[[]]*20
    shapes[0]=[board[0,0],board[1,0],board[2,0],board[3,0],board[4,0],board[5,0],board[6,0],
            board[7,0],board[8,0],board[9,0],board[10,0],board[11,0],board[12,0],board[13,0],
            board[14,0],board[15,0],board[16,0],board[0,1],board[1,1],board[15,1],board[16,1],
            board[1,2],board[16,2],board[16,3],board[14,4],board[15,4],board[16,4],board[14,5],board[16,5]]
    
    shapes[1]=[board[2,1],board[3,1],board[4,1],board[5,1],board[6,1],board[7,1],board[8,1],board[9,1],
            board[10,1],board[11,1],board[12,1],board[13,1],board[14,1],board[2,2],board[3,2],board[14,2],board[15,2],
            board[2,3],board[15,3]]
    
    shapes[2]=[board[0,2],board[0,3],board[1,3],board[3,3],board[4,3],
            board[1,4],board[2,4],board[3,4],
            board[1,5],board[2,5],board[3,5],
            board[1,6],board[2,6],board[3,6]]
    
    shapes[3]=[board[4,2],board[5,2],board[5,3],board[6,3],board[6,4],board[7,4],board[5,5],board[6,5]]

    shapes[4]=[board[6,2],board[7,2],board[8,2],board[9,2],board[10,2],board[11,2],board[12,2],
            board[7,3],board[8,3],board[9,3],board[10,3],board[11,3],
            board[8,4],board[9,4],board[10,4],
            board[9,5]]
    
    shapes[5]=[board[13,2],board[12,3],board[13,3],board[14,3],
            board[12,4],board[13,4],board[12,5],board[13,5],board[12,6],board[13,6],board[12,7],board[13,7],
            board[11,6],board[10,7],board[11,7],board[10,8],board[11,8]]
    
    shapes[6]=[board[0,4],board[0,5],board[0,6],board[0,7],board[0,8],board[0,9],
            board[1,7],board[1,8],board[1,9],board[2,7],board[2,9],board[3,9]]
    
    shapes[7]=[board[4,4],board[5,4],board[4,5],board[4,6],board[4,7],board[3,7],board[3,8],board[2,8]]

    shapes[8]=[board[7,5],board[8,5],board[5,6],board[6,6],board[7,6],board[8,6],board[5,7],board[6,7],board[4,8],board[5,8],board[6,8]]

    shapes[9]=[board[11,4],board[10,5],board[11,5],board[9,6],board[10,6],board[7,7],board[8,7],board[9,7],board[7,8],board[5,9],board[6,9],board[7,9]]

    shapes[10]=[board[15,5],board[14,6],board[15,6],board[16,6],
                board[16,7],board[16,8],board[16,9],board[16,10],board[16,11],board[16,12]]
    
    shapes[11]=[board[4,9],board[4,10],board[5,10],board[6,10],board[7,10],board[8,10],board[9,10],board[8,8],board[8,9],board[8,11],board[8,12],board[7,12],board[9,12]]

    shapes[12]=[board[9,8],board[9,9],board[10,9],board[10,10],board[11,10],board[11,11],board[12,11],board[12,12]]

    shapes[13]=[board[14,7],board[12,8],board[13,8],board[14,8],board[11,9],board[12,9],board[12,10],board[13,10]]

    shapes[14]=[board[15,7],board[15,8],board[13,9],board[14,9],board[15,9],board[15,10],board[15,11],board[14,12],board[15,12],board[14,13],board[15,13],board[16,13]]

    shapes[15]=[board[0,10],board[1,10],board[2,10],board[3,10],board[0,11],board[3,11],board[4,11],board[5,11],board[6,11],board[7,11],
                board[0,12],board[2,12],board[3,12],board[4,12],board[5,12],board[6,12],board[0,13],board[2,13],board[0,14],
                board[0,15],board[1,15],board[0,16],board[1,16],board[2,16],board[3,16],board[4,16]]
    
    shapes[16]=[board[1,11],board[2,11],board[1,12],board[1,13],board[1,14],board[2,14],board[3,14],board[3,13],board[4,13],board[5,13],board[5,14],board[6,14]]

    shapes[17]=[board[9,11],board[10,11],board[10,12],board[6,13],board[7,13],board[8,13],board[9,13],board[10,13],board[8,14],board[10,14],board[10,15],board[11,15]]

    shapes[18]=[board[11,12],board[11,13],board[12,13],board[13,11],board[13,12],board[13,13],board[13,14],board[14,10],board[14,11],board[14,14],board[14,15]]

    shapes[19]=[board[4,14],board[7,14],board[9,14],board[11,14],board[12,14],board[15,14],board[16,14],
                board[2,15],board[3,15],board[4,15],board[5,15],board[6,15],board[7,15],board[8,15],board[9,15],board[12,15],board[13,15],board[15,15],board[16,15],
                board[5,16],board[6,16],board[7,16],board[8,16],board[9,16],board[10,16],board[11,16],board[12,16],board[13,16],board[14,16],board[15,16],board[16,16]]
    
    for i in range(20):
        if sum(shapes[i])!=area_sum:
            return False
    return True


def kai_check(board):
    shapes=[[]]*20
    shapes[3]=[board[4,2],board[5,2],board[5,3],board[6,3],board[6,4],board[7,4],board[5,5],board[6,5]]
    shapes[7]=[board[4,4],board[5,4],board[4,5],board[4,6],board[4,7],board[3,7],board[3,8],board[2,8]]
    shapes[12]=[board[9,8],board[9,9],board[10,9],board[10,10],board[11,10],board[11,11],board[12,11],board[12,12]]
    shapes[13]=[board[14,7],board[12,8],board[13,8],board[14,8],board[11,9],board[12,9],board[12,10],board[13,10]]
    for i in [3,7,12,13]:
        for j in shapes[i]:
            if j!=0 and j!=3:
                return False
    return True

def report(board,steps,count):
    print(board)
    for i in steps:
        print(i,',')
    print('count: ',count)
    print()

#background ends


#operation begins

#These steps are derived from mathematical analysis
steps=[ step(0,0,3,8),
        step(8,5,3,5),
        step(1,11,2,2),
        step(8,2,2,8),
        step(0,3,1,1),
        step(0,14,1,2),
        step(2,7,2,5)]

for former_step in steps:
    block=np.zeros((former_step.size,former_step.size))+former_step.size
    printf(board, former_step, block)


count=len(steps)

flag=0


while not game_req(n, row_sums, rows_req, column_sums, columns_req):
    current_step=step(steps[-1].x,steps[-1].y,steps[-1].size,steps[-1].direction)
    current_step.next()
    backtrack=0
    while putf(board, n, current_step)!=0:
        current_step.next()
        if current_step.size==0:
            current_step=step(steps[count-1].x,steps[count-1].y,steps[count-1].size,steps[count-1].direction)#backtracking
            backtrack+=1
            count-=1
            back(board, current_step)
            current_step.next()#what if this is also 0001
    row_sums=np.sum(board, axis=1)
    column_sums=np.sum(board, axis=0)

    while not (row_column_req(n, row_sums, rows_req, column_sums, columns_req) and area_req(board)):

        back(board, current_step)
        current_step.next()

        while putf(board, n, current_step)!=0:
            current_step.next()
            if current_step.size==0:
                current_step=step(steps[count-1].x,steps[count-1].y,steps[count-1].size,steps[count-1].direction)#backtracking
                backtrack+=1
                count-=1
                back(board, current_step)
                current_step.next()
        row_sums=np.sum(board, axis=1)
        column_sums=np.sum(board, axis=0)

    
    steps=steps[:count]
    steps+=[current_step]
    count+=1


    flag+=1
    if flag%10000==0:
        flag=0
        report(board,steps,count)


print('Done')
report(board,steps,count)









#Below are answer for the puzzle
# steps=[ step(0,0,3,8),
#         step(8,5,3,5),
#         step(1,11,2,2),
#         step(8,2,2,8),
#         step(0,3,1,1),
#         step(0,14,1,2),
#         step(2,7,2,5),

#         step(7,11,2,7) ,
#         step(0,0,1,4) ,
#         step(6,0,1,5) ,
#         step(8,1,1,4) ,
#         step(11,0,1,2) ,
#         step(12,2,1,6) ,
#         step(13,13,1,7) ,
#         step(14,1,1,2) ,
#         step(14,11,1,7) ,]

# for former_step in steps:
#     block=np.zeros((former_step.size,former_step.size))+former_step.size
#     printf(board, former_step, block)

# row_sums=np.sum(board, axis=1)
# column_sums=np.sum(board, axis=0)

# report(board,steps,count)

# print(game_req(n, row_sums, rows_req, column_sums, columns_req))

# print(game_req_2(board))

# blank=1+2+2+3+7+1+1+2+2+2+2+2+1+6+8+7+3+4+2+1+8+2
# ans=  1*2*2*3*7*1*1*2*2*2*2*2*1*6*8*7*3*4*2*1*8*2
# print(blank)

# print(ans)