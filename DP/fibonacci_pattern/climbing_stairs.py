'''
0. Climbing Stairs
Easy
Topics
premium lock icon
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
'''


n=int(input())
arr=[0]*(n+1)
print(arr)
if n in (1,2):
    print(n)
arr[n]=1
arr[n-1]=1
print(arr)
m=n-2
while m>=0:
    print(m)
    arr[m]=arr[m+1]+arr[m+2]
    m-=1
print(arr)

print('total number of possibilties are :',{arr[0]})

'''
to find what are the ways
'''

def paths(n):
    if n==0:
        return [[]]
    elif n<0:
        return []
    res=[]
    for p in paths(n-1):
        res.append([1]+p)
    
    for p in paths(n-2):
        res.append([2]+p)
    return res

m1=paths(n)
print(m1)