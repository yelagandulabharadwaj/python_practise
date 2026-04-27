'''
Edit distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

'''

def editdist(inp1,inp2):
    cols=len(inp1)+1
    rows=len(inp2)+1
    arr=[[0]*cols for row in range(rows) ]
    for i in range(rows):
        arr[i][0]=i
    for j in range(cols):
        arr[0][j]=j
    print(arr)
    for i in range(1,rows):
        for j in range(1,cols):
            if inp2[i-1]==inp1[j-1]:
                arr[i][j]=arr[i-1][j-1]
            else:
                arr[i][j]=1+ min(
                    arr[i-1][j],
                    arr[i-1][j-1],
                    arr[i][j-1]
                )
    print(arr)
    print(arr[rows-1][cols-1])
inp1='horse'
inp2='ros'
editdist(inp1,inp2)