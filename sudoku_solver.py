grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
#Print Board
def matrix_print(matrix):
    for i in range(0,9,3):
        col = matrix[i:i+3]
        for c in col:
            for j in range(0,9,3):
                row = c[j:j+3]
                print(row, end='')
                if j == 6:
                    print(" ")
        print("---------------------------")

def no_conflict(matrix, row_pos, col_pos, num):
        
    #checks for conflict in rows and columns
    for i in range(9):
        row = matrix[row_pos][i]
        if num == row:
            return False
        col = matrix[i][col_pos]
        if num == col:
            return False
    
    #checks for conflict in surrounding square
    row_sqr = (row_pos // 3) * 3   
    col_sqr = (col_pos // 3) * 3

    for i in range(3):
        for j in range(3):
            if matrix[row_sqr+i][col_sqr+j] == num:
                return False 
    return True

#recursive backtracking function to solve the matrix
def solver(matrix):

    for i in range(9):
        for j in range (9):
            if matrix[i][j] == 0:
                for k in range(1, 10):
                    if no_conflict(matrix, i, j, k):
                        matrix[i][j] = k
                        solver(matrix)
                        matrix[i][j] = 0
                return
    matrix_print(matrix)

print("Initial Matrix:")
matrix_print(grid)
print("\nSolved Matrix:")
solver(grid)

