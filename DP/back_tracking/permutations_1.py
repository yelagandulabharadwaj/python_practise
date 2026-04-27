'''
inp=[1,2,3]

output:{[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]}
'''



def permut(arr,res,tmp):
    if len(tmp)==len(arr):
        res.append(tmp[:])
        return

    for num in arr:
        if num in tmp:
            print('-----hereee---',num,tmp)
            continue
        tmp.append(num)
        print(tmp)
        permut(arr,res,tmp)
        tmp.pop()
    return res

inp=[1,2,3]
res=[]
tmp=[]
re=permut(inp,res,tmp)
print(re)