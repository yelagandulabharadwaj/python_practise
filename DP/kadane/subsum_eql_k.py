'''
Count Subarrays having Sum K
Given an array arr[] of postive and negative integers, the objective is to find the number of subarrays having a sum exactly equal to a given number k.

Examples: 

Input : arr[] = [10, 2, -2, -20, 10], k = -10
Output : 3
Explanation: Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum equal to -10.

Input : arr[] = [9, 4, 20, 3, 10, 5], k = 33
Output : 2
Explanation: Subarrays: arr[0...2], arr[2...4] have sum equal to 33.

Input : arr[] = [1, 3, 5], k = 2
Output : 0
Explanation: No subarrays with 0 sum.

'''
def subsum_k(arr,k):
    pre_sum={0:1}
    cur_sum=0
    tot=0
    for i in range(0,len(arr)):
        cur_sum=cur_sum+arr[i]
        if cur_sum-k ==0:
            tot+=pre_sum[0]
        pre_sum[cur_sum]=pre_sum.get(cur_sum,0)+1
    print(tot)
    print(pre_sum)

# arr=[10, 2, -2, -20, 10]
# k = -10
# arr=[2, 3, -5, 5,-5, 1,4]
# k=5
# arr=[1,3,5]
# k=2
arr=[9, 4, 20, 3, 10, 5]
k=33

subsum_k(arr,k)