'''
Painting Fence Algorithm
Last Updated : 11 Nov, 2024
Given a fence with n posts and k colors, the task is to find out the number of ways of painting the fence so that not more than two consecutive posts have the same color.

Examples:

Input: n = 2, k = 4
Output: 16
Explanation: We have 4 colors and 2 posts.
Ways when both posts have same color: 4 
Ways when both posts have diff color: 4(choices for 1st post) * 3(choices for 2nd post) = 12

Input: n = 3, k = 2
Output: 6
Explanation: The following image depicts the 6 possible ways of painting 3 posts with 2 colors:

'''

def fence(n,k):
    if n==1:
        return k
    elif n==2:
        return k**2
    else:
        return fence(n-1,k)*(k-1) + fence(n-2,k)*(k-1)
    
# print(fence(3,2))
print(fence(2,4))