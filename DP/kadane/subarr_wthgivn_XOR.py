'''
Given an array of integers arr[] and a number k, the task is to count the number of subarrays having XOR of their elements as k.
Input: arr[] = [4, 2, 2, 6, 4], k = 6
Output: 4
Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6].

Input: arr[] = [5, 6, 7, 8, 9], k = 5
Output: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9].

'''

def xorsub(arr,k):
    prexor={0:1}
    res=0
    c=0
    for i in arr:
        res^=i
        if res^k in prexor:
            c+=prexor[res^k]
        prexor[res]=prexor.get(res,0)+1
    print(prexor,c)


# arr = [4, 2, 2, 6, 4] 
# k = 6
# xorsub(arr,k)
arr= [5, 6, 7, 8, 9]
k = 5
xorsub(arr,k)