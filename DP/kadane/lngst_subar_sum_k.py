'''
Given an array arr[] containing integers and an integer k, 
your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k.
 If there is no subarray with sum equal to k, return 0.

 Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.

Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Subarrays with sum = -5 are [-5] and [-5, 8, -14, 2, 4]. The length of the longest subarray with a sum of -5 is 5.

Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].

'''

def lngstarr(arr,k):
    pre_sum={0:[-1]}
    res=[]
    cur_sum=0
    for  i in range(len(arr)):
        cur_sum+=arr[i]
        if cur_sum-k in pre_sum:
            for st in pre_sum[cur_sum-k]:
                res.append(arr[st+1:i+1])
        if cur_sum-k not in pre_sum:
            pre_sum[cur_sum-k]=i
        else:
            pre_sum[cur_sum-k].append(i)
    print(res)

arr=[-5, 8, -14, 2, 4, 12]
k = -5
lngstarr(arr,k)
arr=[10, 5, 2, 7, 1, -10]
k =15
lngstarr(arr,k)
arr=[0,1,2,3,4]
k=4
lngstarr(arr,k)