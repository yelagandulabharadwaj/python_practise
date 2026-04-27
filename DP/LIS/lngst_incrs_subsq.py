'''
Longest Increasing Subsequence (LIS)

Given an array arr[] of size n, find the length of the Longest Increasing Subsequence (LIS) 
i.e., the longest possible subsequence in which the elements of the subsequence are sorted in strictly increasing order.

Input: arr[] = [3, 10, 2, 1, 20]
Output: 3
Explanation: The longest increasing subsequence is 3, 10, 20

Input: arr[] = [30, 20, 10]
Output:1
Explanation: The longest increasing subsequences are [30], [20] and [10]

Input: arr[] = [2, 2, 2]
Output: 1
Explanation:  We consider only strictly increasing subsequences, therefore the longest increasing subsequence is [2].

Input: arr[] = [3, 4, 5, 1, 2, 3, 4]
Output: 4
Explanation: The longest strictly increasing subsequence is [1, 2, 3, 4], which gives a maximum length of 4.
 (Note: [3, 4, 5] is also an increasing subsequence, but its length is only 3).


''' 


def long_subseq(arr):
    res=[1]*len(arr)
    parent = [-1] *len(arr)
    for i in range(1,len(arr)):
        j=0
        m=[]
        while j<i:
            if arr[j]<arr[i]:
                if res[j]+1 > res[i]:
                    res[i]=res[j]+1
                    parent[i]=j
            j+=1
        # print(m)
        # lt[i].append(m)
    print("result: ",res," count: ",max(res))
    # print(lt)

    '''
    to print what are those elements
    '''
    # last=len(res)-2
    # path=[]
    # main_ele=res.index(res[last+1])
    # path.append(arr[main_ele])
    # while last>=0 :
    #     if res[last+1]==1:
    #         break
    #     if (res[last]<res[last+1]):
    #         path.append(arr[last])
        
    #     last-=1

    val_in=max(res)
    ind=res.index(val_in)
    path=[]
    while ind !=-1:
        path.append(arr[ind])
        ind=parent[ind]
    print("path is : ",path)
    print("\n")



arr=[3, 4, 5, 1, 2, 3, 4]
long_subseq(arr)
arr=[3, 10, 2, 1, 20]
long_subseq(arr)
arr=[30, 20, 10]
long_subseq(arr)
arr=[2, 2, 2]
long_subseq(arr)
arr=[1, 101, 2, 3, 105]
long_subseq(arr)
arr=[0,1,0,3,2,3]
long_subseq(arr)