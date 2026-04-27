'''
find number od subarrays where sum of sub array is 0
Examples:

Input: arr[] = [6, -1, -3, 4, -2, 2, 4, 6, -12, -7]

Output: 4

Explanation: The 4 subarrays are [-1, -3, 4], [-2, 2], [2, 4, 6, -12], 
and [-1, -3, 4, -2, 2]
 
'''

'''
worst appraoch to solve
'''

def subsum(arr):
    c=0
    for i in range(0,len(arr)-1):
        j=i+1
        res=arr[i]
        while j<len(arr):
            res+=arr[j]
            # print(res,arr[j])
            if res==0:
                c+=1
            j+=1
        
    print(c)

arr=[6, -1, -3, 4, -2, 2, 4, 6, -12, -7]
# arr=[6, -1, -3,-2]
# subsum(arr)


def prefixsum(arr):
    n=len(arr)
    pre_arr=[0]*n
    pre_arr[0]=arr[0]
    for i in range(1,n):
        pre_arr[i]=pre_arr[i-1]+arr[i]
    print(arr)
    print(pre_arr)
    return pre_arr

# arr=[3,-1,-2,4,-4]
arr=[6, -1, -3, 4, -2, 2, 4, 6, -12, -7]
# m=prefixsum(arr)

'''
Below is the optimal approach for finding number of ways for subarry sum =0
'''

def presum(arr):
    c=0
    freq={0:1}
    pre_sum=0
    for i in arr:
        pre_sum+=i
        if pre_sum in freq:
            c+=freq[pre_sum]
        # if pre_sum==0:
        #     c+=1
        freq[pre_sum]=freq.setdefault(pre_sum,0)+1
    print(freq,c)

arr=[3,-1,-2,4,-4]
presum(arr)

'''
below approach is to return whcih elemets can sum of subarray be 0
'''
#storing there values

def subarraysumZero(arr):
    pre_sum=0
    freq={0:[-1]}
    res=[]
    for i in range(len(arr)):
        pre_sum+=arr[i]
        if pre_sum in freq:
            for st in freq[pre_sum]:
                res.append(arr[st+1:i+1])

        if pre_sum not in freq:
            freq[pre_sum] = []
        freq[pre_sum].append(i)
    return res

# arr=[3,-1,-2,4,-4]
arr=[6, -1, -3, 4, -2, 2, 4, 6, -12, -7]
print(subarraysumZero(arr))