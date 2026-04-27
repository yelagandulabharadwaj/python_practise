



def canmake(arr,i,rem):
    if rem==0: return True
    if rem<0: return False
    if i<0: return False
    return canmake(arr,i-1,rem-arr[i]) or canmake(arr,i-1,rem)

# arr=[1,5,11,5]
# arr=[1,2,3,5]
# arr=[3, 3, 3, 3]  
arr=[2, 2, 3, 5]
n=len(arr)
i=n-1
rem=sum(arr)//2
if rem%2!=0:
    print(False)
else:
    print(canmake(arr,i,rem))