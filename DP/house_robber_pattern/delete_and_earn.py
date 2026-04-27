'''
740. Delete and Earn
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

'''

# def get_unique(arr):
#     s=set()
#     for i in arr:
#         s.add(i)
#     print(list(s),arr)
#     return list(s)


# def remov_dup(k,nums):
#     # print(nums,k)
#     return [x for x in nums if (x != k+1 and x!=k-1)]

# def maxunique(arr,res):
#     # print(res)
#     unq=get_unique(arr)
#     # print(unq)
#     if len(unq)==1:
#         return unq[0]
#     if len(unq)==0:
#         return 0
    
#     for j in unq:
#         tmp=remov_dup(j,arr)
#         print(tmp)
#         aa=j+maxunique(tmp,res)
#         res.append(aa)
#     # print(res)
#     return res


def houserobing(arr):
    r=[0]*(len(arr)+1)
    r[0]=arr[0]
    r[1]=max(r[0],arr[1])
    print('----',r,arr,r[1])
    for j in range(2,len(arr)):
        r[j]=max(arr[j]+r[j-2] , r[j-1])
    print(r)
    return r[len(arr)-1]

# nums = [2,2,3,3,3,4]
nums = [3,4,2]
res=[0]*(10**1)

for i in nums:
    res[i]+=i
res1=[x for x in res if x!=0]
print(res1)
m=houserobing(res1)
print(m)
