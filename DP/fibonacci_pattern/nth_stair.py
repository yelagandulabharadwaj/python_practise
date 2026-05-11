'''
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. 
The task is to implement a method to count how many possible ways the child can run up the stairs.

Examples: 

Input: 4
Output: 7
Explanation: There are seven ways: {1, 1, 1, 1}, {1, 2, 1}, {2, 1, 1}, {1, 1, 2}, {2, 2}, {3, 1}, {1, 3}.

Input: 3
Output: 4
Explanation: There are four ways: {1, 1, 1}, {1, 2}, {2, 1}, {3}.

'''

def nthstair(n):
    arr=[-1]*(n+1)

    def findpaths(arr,n):    
        if n==0:
            return 1
        if n<0:
            return 0
        if arr[n]!=-1:
            # print(n,arr[-1])
            return arr[n]
        arr[n]=max(0,findpaths(arr,n-1)+findpaths(arr,n-2)+findpaths(arr,n-3))
        print(arr)
        return arr[n]
        
    return findpaths(arr,n)

# nthstair(4)


def nthstairways(n):
    arr=[-1]*(n+1)

    def findways(arr,n):
        if n==0:
            return [[]]
        if n<0:
            return []
        res=[]
        for p in findways(arr,n-1):
            res.append([1]+p)
        for p in findways(arr,n-2):
            res.append([2]+p)
        for p in findways(arr,n-3):
            res.append([3]+p)
        
        # arr[n]=max(0,findways(arr,n-1)+findways(arr,n-2)+findways(arr,n-3))
        print(res)
        return res
        
    return findways(arr,n)
nthstairways(4)