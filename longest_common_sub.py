# nums = [100, 4, 200, 1, 3, 2]
nums=[1,2,3,10,11]

res=dict()
for i in nums:
    
    num_set=nums
    if i-1 not in num_set:
        j=i
        m=[]
        while j in num_set:
            m.append(j)
            j+=1
        res[i]=m
print(res)

ll=lambda x:x[1]
s= ll(res)
print(max(res.values(),key=len))
print(s)
