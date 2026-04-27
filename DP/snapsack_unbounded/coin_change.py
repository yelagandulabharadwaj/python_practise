


'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

Bruteforce
'''
# arr=[5,1,3,2]
# amt=11

# arr=[2]
# amt=3

arr=[1]
amt=0
arr=sorted(arr,reverse=True)
c=0
while amt>min(arr):
    for i in arr:
        if amt>i:
            amt-=i
            c+=1
            break
if amt>0:
    if amt==min(arr):
        c+=1
    else:
        c=-1
    print(c)
else:
    print(-1)

'''
Belo optimal sol
'''


def coinchange(coins,amt):
    dp=[1000]*(amt+1)
    dp[0]=0
    print(dp)
    for i in range(1,amt+1):
        for coin in coins:
            if coin<=i:
                print('coin:',i)
                print('dp value:',f'min of {dp[i],1+dp[i-coin]}')
                dp[i]=min(dp[i],1+dp[i-coin])
                
    
    print(dp)
    
coins=[1,2,5]
amt=11
coinchange(coins,amt)
