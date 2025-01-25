x ={"first" : [1,2,3] , "second": "me" , "third" :50.2 ,"forth": 0,"fifth" : [4,5,6]}
v = list(x.values())
v.reverse()
# print(v)
# for i in range(len(v)) :
    # p = list(x.keys())
    # x[p[i]] = v[i]
# print(x)
# 

for i in range(len(v)) :
    p = list(x.keys())
    x[p[i]] = v[i]
print(x)

