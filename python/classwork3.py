name = { "sahar": 15 , "malaz" : 16}
print(name)

for i in name :
    print(i)

for i in name.values() :
    print(i)
#الطريقة الاولي 
print(name["sahar"])
#الطريقة الثانية
print(name.get("malaz"))
print("="*60)
i = {"malaz": 30,"wala":20 ,"sahar":"sahora"}
# for u in i.values() :
#     # u[i]
#     print(i.get(u))
 
s ={"a":"a" , "b" : "b"  , "c" : "c"}
for i in s :
    if i == "c" :
        print(s[i])
   
print("="*60)
o = { "age": [10,20,14] , "number": 12 ,"float" :20.5 }
p =1
for i in o :
#     if isinstance(o[i],int) :
   
#       print(o[i])
    if isinstance(o[i],list) :
        # print(o[i])
        for j in range(len(o[i]) ):
         o[i][j] +=1  
        #  u = p + o[i][j] اذا شغلته كدا ح يغير علي القائمة لكن م ح يعدل علي الاصلي #
        print(o[i])
       
print(o)

# o = { "age": [10,20,14] , "number": 12 ,"dic" : {"namn" :"malaz ","frind" :"sahar" }}
