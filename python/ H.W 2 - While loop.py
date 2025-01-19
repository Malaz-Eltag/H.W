
o = 1
c = 0
while c < 12 :
    print(o)
    o+= 1
    c+= 1

    if c == 3 :
        o = 1
        print(o)
        o+= 1



print("="*50)

c = 1
while c < 7 :
    for w in range(10) :
        if w % 2 == 0:
            print(w, end = " ")  # output 0 2 4 6 8
            # print(w+1, end = " ") output 2 4 6 8 10 
            c += 1
            if c == 6 :
                print("")
                c = 3
                c += 2
                for r in range (10) :
                    if r% 2 == 1:
                        print(r, end = " ")  
                     #  print(r+1, end = " ") output 1 3 5 7 9 
                        c += 1

print("")
print("="*50)
 
 
 
## one loop  "While loop " ##
a = 1
while a <=12 :
    if a ==1 or a == 2 or a == 4  :
        print(" ",end="")
    else :
        print("1",end="")
    if  a == 3 or a ==7  :
        print("")
    a += 1

print("")
print("="*50)

## one loop  "For loop " ##
for g in range (12) :
    if g == 0 or g == 1 or g == 3 :
        print(" ",end="")
    else :
        print("1",end="")
    if g == 2 or g == 6 :
        print("")
    g += 1


# p = 1
# d = 1
# while p < 4:
#     print("  ",end="")
#     print(d, end="")
#     p += 1
#     print("")
#     for y in range(3):
#             p += 1
#             if p == 3:
#                 print(f" ",end="")
#             print(d,end="")  
#             p += 1
#     print("")
#     for i in range (5) :
#         print(d,end="")
print("")

print("="*50)

y = 0
i =1
while y < 3:
 
    y+=1
    for q in range(1):
        if y == 1: 
            print("  ",end="1")
 
    print("")
    
    for x in range(3) :
         print(i,end=" ")
    
    for t in range(1):
        if y == 3: 
            print("")
 
            print("  ",end="1")      
 
print("")
print("="*50)
 
k = 1
while k < 3:
    print("   ", end="1")
    k += 1
    print("")
    for y in range(3):
            k += 1
            if k == 3:
                print(f" ",end="")
            print(f"1",end="")  
            k += 1
    print("")
    for i in range (4) :
        print(f"1",end="")

print("")
print("="*50)


k = 1
z = 1
while k < 4:
    print("  ",end="")
    print(z, end="")
    k += 1
    print("")
    for y in range(3):
            k += 1
            if k == 3:
                print(f" ",end="")
            print(z,end="")  
            k += 1
    print("")
    for i in range (5) :
        print(z,end="")
    print("")
    for i in range (5) :
            print(z,end="")
    print("")
    print(" ",end="" ) 

    for u in range (2) :
        print( z,end="")
    # print( z,end="")
    k += 1
    # print("")
    
    for y in range(1):
                k += 1
                if k == 3:
                    print(f"  ",end="  ")
                print(z,end=" ")  
                k+= 1
    print("  ")                     
    print("  ",end="" ) 
    print(z)
        
        
        

    
                                                           