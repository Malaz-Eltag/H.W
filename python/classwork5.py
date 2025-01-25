x ={"first" : [1,2,3] , "second": "me" , "third" :50.2 ,"forth": 0,"fifth" : [4,5,6]}
print(f"\n{x}\n\n x after swap is :\n")
values =list(x.values()) 
values.reverse() 
for i in range(len(values)) :
    p = list(x.keys())
    x[p[i]] = values[i]
print(x)