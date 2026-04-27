

def targetsum(arr,k):
    n,i=len(arr),0
    dpsum={0:1}
    tmp=dpsum
    while i<n:
        tmp={}
        for key,val in dpsum.items():
            s=key+arr[i]
            tmp[s]=tmp.get(s,0) + dpsum[key]
            s=key-arr[i]
            tmp[s]=tmp.get(s,0) + dpsum[key]
        dpsum=tmp
        i+=1
    print(dpsum)
    return dpsum.get(k,0)

# arr=[1,1,1,1,1]
arr=[1,2,3]
k=3
print(targetsum(arr,k))