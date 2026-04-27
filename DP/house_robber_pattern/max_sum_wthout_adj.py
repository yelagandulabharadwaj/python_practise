'''
Max Sum without Adjacents

Given an array arr containing positive integers.
 Find the maximum sum of elements of any possible subsequence such that no two numbers in the subsequence should be adjacent in array arr[].

 Input: arr[] = [5, 5, 10, 100, 10, 5]
Output: 110
Explanation: If you take indices 0, 3 and 5, then = 5+100+5 = 110.

Input: arr[] = [3, 2, 7, 10]
Output: 13
Explanation: 3 and 10 forms a non continuous subsequence with maximum sum.

Input: arr[] = [9, 1, 6, 10]
Output: 19
Explanation: 9 and 10 forms a non continuous subsequence with maximum sum.

[5, 5, 10, 100, 10, 5]
5   5  15  105  105 110

[3, 2, 7, 10]
3  2   10
'''

def maxsum(arr):
    res=[0]*(len(arr))
    res[0]=arr[0]
    res[1]=max(arr[0],arr[1])
    for i in range(2,len(arr)):
        # print(i,res[:i-1])
        res[i]=max(res[i-1],res[i-2]+arr[i])
        # print(res,arr[:i-1])
    print(res)
    return res[-1]
nums=[5, 5, 10, 100, 10, 5]
print(maxsum(nums))
nums=[9, 1, 6, 10]
print(maxsum(nums))
nums=[3, 2, 7, 10]
print(maxsum(nums))

nums=[5, 3, 4, 11, 2]
print(maxsum(nums))
nums= [6, 7, 1, 3, 8, 2, 4]
print(maxsum(nums))