'''
Subsets of a given Array

Given an integer array arr[], find all the subsets of the array.

A subset is any selection from an array, where the order does not matter, and no element appears more than once.
A subset can include any number of elements, from none (the empty subset) to all.
Input: arr[] = [1, 2, 3]
Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
Explanation: The subsets of [1, 2, 3] are: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

Input: arr[] = [2, 4]
Output: [[], [2], [2, 4], [4]]
Explanation: The subsets of [2, 4] are: [[], [2], [2, 4], [4]]



'''

def subarrrec(i,arr,res,subset):
    if i==len(arr):
        res.append(list(subset))
        return
    subset.append(arr[i])
    subarrrec(i+1,arr,res,subset)
    subset.pop()
    subarrrec(i+1,arr,res,subset)


res,subset=[],[]
# arr=[1,2,3]
arr=[2, 4]
subarrrec(0,arr,res,subset)
print(res)

'''

small task
------------
Find all subsequences with sum equals to K
Given an array arr[] of length n and a number k, the task is to find all the subsequences of the array with sum of its elements equal to k.

Note: A subsequence is a subset that can be derived from an array by removing zero or more elements, without changing the order of the remaining elements.

Input: arr[] = [1, 2, 3], k = 3 
Output: [ [1, 2], [3] ]
Explanation: All the subsequences of the given array are:
[ [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3], [] ]
Out of which only two subsequences have sum of their elements equal to 3.

Input: arr[] = [1, 2, 3], k = 7
Output: []
Explanation: Sum of all the elements of the array is 6, which is smaller than the required sum, thus they are no subsequences with sum of its elements equal to 7.

Input: arr[] = [17, 18, 6, 11, 2, 4], k = 6  
Output: [ [2, 4], [6] ] 


'''

def sumsubsetrec(i1,arr1,res1,subset1,k1):
    if i1==len(arr1):
        if k1== sum(subset1):
            res1.append(subset1[:])
        return
    
    subset1.append(arr1[i1])
    sumsubsetrec(i1+1,arr1,res1,subset1,k1)
    subset1.pop()
    sumsubsetrec(i1+1,arr1,res1,subset1,k1)

res1,subset1=[],[]
arr1 = [1, 2, 3]
k1 = 3
sumsubsetrec(0,arr1,res1,subset1,k1)
print(res1)

#bruteforce

def brute(arr):
    n=len(arr)
    for mask in range(1 << n):
        print(mask)
brute([1,2,3])