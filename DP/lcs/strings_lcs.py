
'''
Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.


Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
'''
inp1='abcdaf'
inp2='acbcf'

# inp1='abc'
# inp2='abc'

# inp1='abc'
# inp2='def'

# inp1 = "abcdgh"
# inp2 = "aedfhr"

rows=len(inp1)+1
cols=len(inp2)+1

arr=[[0]*cols for row in range(rows)]

for i in range(1,rows):
    for j in range(1,cols):
        if inp1[i-1]==inp2[j-1]:
            arr[i][j]=1+arr[i-1][j-1]
        else:
            arr[i][j]=max(arr[i-1][j],arr[i][j-1])
print(arr)

'''
here is that string

'''
loc_str=''
i,j=rows-1,cols-1
while (i>0 and j>0):
    if inp1[i-1]==inp2[j-1]:
        loc_str+=inp1[i-1]
        i-=1
        j-=1
    elif arr[i-1][j]>arr[i][j-1]:
        i-=1
    else:
        j-=1
        
    # print(loc_str)
print(loc_str[::-1])