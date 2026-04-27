'''
Maximum Sum Increasing Subsequence
Last Updated : 10 Nov, 2025
Given an array arr[] which consists of positive integers.
 Find the sum of the maximum sum subsequence of the given array such that the integers in the subsequence are sorted in strictly increasing order.
Input: arr[] = [1, 101, 2, 3, 100]
Output: 106
Explanation: The maximum sum of a increasing sequence is obtained from [1, 2, 3, 100].

Input: arr[] = [4, 1, 2, 3]
Output: 6
Explanation: The maximum sum of a increasing sequence is obtained from [1, 2, 3].
'''
import copy
def maximumsum(arr):
    su_arr=copy.deepcopy(arr)
    for i in range(1,len(arr)):
        j=0
        while j<i:
            # print(arr[i],arr[j],su_arr[i])
            if arr[j]<arr[i]:
                if su_arr[i]<(arr[i]+su_arr[j]):
                    su_arr[i]=(su_arr[j]+arr[i])

            j+=1
    print(su_arr)

arr=[4, 1, 2, 3]
maximumsum(arr)
arr=[1, 101, 2, 3, 100]
maximumsum(arr)
arr=[1, 101, 2, 3, 105]
maximumsum(arr)