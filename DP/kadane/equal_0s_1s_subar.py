'''

Subarrays with equal 1s and 0s

Input: arr[] = [1, 0, 0, 1, 0, 1, 1]
Output: 8
Explanation: The index range for the 8 sub-arrays are: (0, 1), (2, 3), (0, 3), (3, 4), (4, 5) ,(2, 5), (0, 5), (1, 6)
'''

#bruteforce

def subar(arr):
    c=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[:i].count(0) == arr[:j].count(1):
                c+=1
    print(c)

arr=[1, 0, 0, 1, 0, 1, 1]
subar(arr)