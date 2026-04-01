a=[[1,2,3],[4,5,6],[9,8,7]]

s=[]
for m in a:
    for aa in m:
        s.append(aa)

print(s)

b=[1,[2,[3,4],5],6]
res=[]
def flat(b,res):
    for item in b:
        if isinstance(item,list):
            flat(item,res)
        else:
            res.append(item)
    return res
print(flat(b,res))
