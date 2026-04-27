'''
Stock Buy and Sell - Max one Transaction Allowed

Given an array prices[] of non-negative integers, representing the prices of the stocks on different days, find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.
Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: Buy for price 1 and sell for price 9. 

Input: prices[] = [7, 6, 4, 3, 1]
Output: 0
Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

Input: prices[] = [1, 3, 6, 9, 11]
Output: 10
Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1]

            [7, 10, 1 , 3,   6,  9,   2]
buy          7      1            
cur_pft      0  3       2    5   8    1
max_pft      0  3     (3>2)  5   8    (8>1)
--------------------------------------------
max_proft is =8
'''

def getmax(stks):
    buy=stks[0]
    cur_prft=0
    max_prft=0
    for i in range(1,len(stks)):
        if buy>stks[i]:
            buy=stks[i]
        else:
            cur_prft=stks[i]-buy
            if max_prft<cur_prft:
                max_prft=cur_prft
    return max_prft
print(getmax([7, 10, 1 , 3,   6,  9,   2]))
print(getmax([1, 3, 6, 9, 11]))
print(getmax([7, 6, 4, 3, 1]))
