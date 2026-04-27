'''
91. Decode Ways
Medium
Topics
premium lock icon
Companies
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

'''

# def decode(stng):
#     arr=[-1]*len(stng)
#     n=len(stng)-1#4
#     if "0" not in stng:
#         arr[n],arr[n-1]=1,2
#         n=n-2#3
#         while(n>=0):
#             arr[n]=arr[n+1]+arr[n+2]
#             n-=1
    # print(arr)

# def decode(i,stng,n,arr):
#     if stng[i:].startswith("0"):
#         return 0
#     if i>n-1:
#         if stng[i]!=0:
#             return 1
#         else:
#             return 0
#     arr[i]=decode(i,stng[i:],len(stng[i:],arr)) + decode(i+1,stng[i+1:],len(stng[i+1:],arr))


def decode(stng):
    n=len(stng)
    arr=[0]*(n+1)
    arr[0]=1
    
    if stng[0]!='0':
        arr[1]=1
    else:
        arr[1]=0
    i=2
    while i<=n:
        
        if stng[i-1]!='0' :
            arr[i]+=arr[i-1]
        if  10<=int(stng[i-2:i])<=26:
            arr[i]+=arr[i-2]
        i+=1
    print(arr)

decode("12123")

decode("11106")

decode("122016")