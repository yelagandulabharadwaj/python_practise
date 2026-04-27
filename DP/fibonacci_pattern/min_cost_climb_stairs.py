

'''
MIn cost climning stairs
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

'''

def costclimb(arr):
    n=len(arr)
    i=0
    tot=[-1]*n
    def climb(i):
        
        if i>=n:
            return 0
        if tot[i]!=-1:
            return tot[i]
        tot[i]=arr[i]+min(climb(i+1),climb(i+2))
        print(tot,tot[i])
        return tot[i]
    return min(climb(0),climb(1))

a=[10,15,20]
# a=[1,3,2,4]
print(costclimb(a))