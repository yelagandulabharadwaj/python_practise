
'''
198. House Robber
Medium
Topics
premium lock icon
Companies
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

knowledge:

H1  H2   H3.......

for H3 we can choose among 2 things

1. amnt looted till H2
2. amnt looted till H1 + looting H3

get max(1,2)
'''

inp=input().split()
arr=[]
for i in inp:
    arr.append(int(i))

tot=[0]*len(arr)
paths=[]
if len(arr)==1:
    print(arr)
else:
    if len(arr)==2:
        tot[1]=max(arr[0],arr[1])
    else:
        tot[0],tot[1]=arr[0],max(arr[0],arr[1])
        # paths.extend([arr[0]])
        # paths.extend([max(arr[0],arr[1])])

        for i in range(2,len(arr)):
            tot[i]=max(tot[i-2]+arr[i],tot[i-1])

            # m1=tot[i-2]+arr[i]
            # m2=tot[i-1]
            # if(m1>m2):
            #     paths.extend([arr[i-2]])
            #     paths.extend([arr[i]])
            # else:
            #     paths.extend([arr[i-1]])

print(tot)
# print(paths)
