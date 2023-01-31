# This program solves the 8-Queens problem using backtracking
# The 8-Queens problem is to place 8 queens on an 8x8 chessboard such that no two queens attack each other

input="Enter the number of queens: "
n = int(input)  # get the number of queens from the user
board = [[0]*n for _ in range(n)]  # create an empty chessboard with n rows and n columns

# Check if a queen placed at i, j is under attack from any other queen
def attack (i, j):
    # Check horizontally
    for k in range(0,n):
        if board [i][k]==1 or board[k][j]==1:
            return True
    # Check diagonally
    for k in range (0,n):
        for l in range(0, n):
            if (k+l==i+j) or (k-1==i-j):
                if board[k][l]==1:
                    return True
    # If no queen is attacking, return False
    return False

# Solve the n-Queens problem using backtracking
def n_queens(a):
    if a==0:  # base case: if all queens are placed, return True
        return True
    for i in range(0,n):
        for j in range(0, n):
            if(not(attack(i,j))) and (board [i][j]!=1):  # if this position is not under attack and not already occupied by a queen
                board[i][j]=1  # place a queen here
                if n_queens(a-1)==True:  # move to the next queen
                    return True
                board[i][j]=0  # if placing a queen here does not lead to a solution, backtrack and try another position
        return False

# Call the n_queens function with n as the argument
n_queens(n)

# Print the final solution
for i in board:
    print(i)
