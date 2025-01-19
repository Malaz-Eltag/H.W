list =[ 1 , "Sahar" , 1.7 , 2 , 5.3, "Fatima" ,23.4  ,"Wala" ,8.8, "Mona" ,2.8 , 5 ,"Mina"]
p = 0
for i in (list)  :
    if isinstance(i, str) :
        print(f"This is not a number : {i}")
    if isinstance(i, int ) or isinstance(i, float ):
        p+= i
print(f"The sum of the numbers is : {p}")