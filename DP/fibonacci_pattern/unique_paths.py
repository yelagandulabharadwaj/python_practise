'''
62. Unique Paths
Medium
Topics
premium lock icon
Companies
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

'''



m,n=3,7

res=[[0]*n for i in range(m)]
for i in range(m):
    res[i][0]=1
for j in range(n):
    res[0][j]=1

for i in range(1,m):
    for j in range(1,n):
        res[i][j]=res[i][j-1]+res[i-1][j]

print(res)

'''

63. Unique Paths II
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

'''

# inp_arr=[[0,0,0],[0,5,0],[0,0,0]]
inp_arr= [[0,5],[0,0]]

# 5 is obstacel here

m=len(inp_arr[0])
n=len(inp_arr)
res=[[0]*n for i in range(m)]
# print(inp_arr)
for i in range(m):
    for j in range(n):
        if (i==0 or j==0) and (inp_arr[i][j]!=5):
            res[i][j]=1
        elif (inp_arr[i][j]==5):
            res[i][j]=0
            # print(inp_arr,res)
        else:
            res[i][j]=res[i-1][j]+res[i][j-1]
print(res)
        
