# x ={"name" :3,"age": 20,"g" :[10,2,18]  }
# for i in x :
#     if isinstance(x[i],list) :
#         for j in range ( len(x[i])) :
#            print(x[i][j])

# x["first"] = [4,5,6]
# x["malaz"] = 20
# x["fifth"] = [4,5,9]
# print(x) 
# u = 0
# for i in x:
#     x[i] = 0
# print(x)
# print("="*50)
# x ={"first" : [1,2,3] , "second": "me" , "third" :50.2 ,"forth": 0,"fifth" : [4,5,6]}
# for i in x :
#     if isinstance(x[i],list) :
#     # if isinstance(x[i],list) :
#         for j in range ( len(x[i])) :
#         #    print(x[i][j])
# u =0
# x ={"first" : [1,2,3] , "second": "me" , "third" :50.2 ,"forth": 0,"fifth" : [4,5,6]}
# m =1
# o = list(x.values())
# o.reverse()  

# for i in range (len(o)):
    #  p = list(x.keys())
    #  print(x)
    #  x[p[i]] = o[i]
# print(x)
# 
        # print(x[p[i]]) #= p[j]
# print(x[p])
         
    
# print(x)
        # if i.values() :
        #   for j in range(len(i)) :
            # print(i[j])

#         for j in range(len(x[i])) :
            # x[j] = p
#             print(x[i[j]])

        
    # print(p)
   





# x ={"first" : [1,2,3] , "second": "me" , "third" :50.2 ,"forth": 0,"fifth" : [4,5,6]}
# print(f"\n{x}\n\n x after swap is :\n")
# # y =[]
# # for i in x:
#     # y.append(x[i])
# # list_length =len(y)
# y =list(x.values()) 
# for i in range(len(y) // 2): 
#     temp = y[i]
#     y[i] = y[len(y) - i - 1]
#     y[len(y) - i - 1] = temp 

# for i in range(len(y)) :
#    x[list(x.keys())[i]] = y[i]
# print(x)




# x ={"first" : [1,2,3] , "second": "me" , "third" :50.2 ,"forth": 0,"fifth" : [4,5,6]}
# print(f"\n{x}\n\n x after swap is :\n")
# values =list(x.values()) 
# values.reverse() 
# for i in range(len(values)) :
#    p = list(x.keys())
#    x[p[i]] = values[i]
# print(x)





# x ={"first" : [1,2,3] , "second": "me" , "third" :50.2 ,"forth": 0,"fifth" : [4,5,6]}
# print(f"\n{x}\n\n x after swap is :\n")
# values =list(x.values()) 
# values.reverse()
# for i ,key in enumerate(x) :
#     x[key] = values[i]
# print(x)



x ={"first" : [1,2,3] , "second": "me" , "third" :50.2 ,"forth": 0,"fifth" : [4,5,6]}
print(f"\n{x}\n\n x after swap is :\n")
y =list(x.values()) 
print(y)
for i in range(len(y) // 2): 
    temp = y[i]
    y[i] = y[len(y) - i - 1]
    y[len(y) - i - 1] = y[i]# y[len(y) - i - 1] #temp 

for i in range(len(y)) :
   x[list(x.keys())[i]] =  y[i]
print(x)
















x ={"first" : [1,2,3] , "second": "me" , "third" :50.2 ,"forth": 0,"fifth" : [4,5,6]}
print(f"\n{x}\n\n x after swap is :\n")
y =list(x.values()) 
# print(y)
for i in range(len(y) // 2): 
  t =  y[len(y) - i - 1]  
for i in range(len(y)) :
  x[list(x.keys())[i]]  = t #y[len(y) - i - 1] 
print(x)
