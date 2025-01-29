def add(a,b):
    
    return a + b
x=add(5,7)
print(add(5,7))
print(x ,x+5 )

print("="*50)
class car :
    def __init__(self,name,year,serial):
        self.name=name 
        self.year=year
        self.serial=serial
    def get_info(self):
        # return (f"Name: {self.name}, Year: {self.year}, Serial: {self.serial}")
      
        print (f"Name: {self.name},Year: {self.year}, Serial: {self.serial}")
    
    def __str__(self):
         return f"Name: {self.name} "
NewCar = car("BMW", 2023,69998224)
# NewCar.get_info()
print(NewCar)


     
# class dress :
#     #properties
#     def __init__(self,style,size,pirce):
#         self.style=style 
#         self.size=size
#         self.pirce=pirce
    
#     #Methods
#     def get_info(self):
#         print (f"style: {self.style}, size: {self.size}, pirce: {self.pirce}")
#     def __str__(self):
#          return f"style: {self.style} "
    
# dress_1 = dress("tall", "S",500)
# dress_1.get_info()
# print(dress_1)
# print(dress_1.style,dress_1.size,dress_1.pirce)
# dress_1.style ="short"
# dress_1.size="M"
# dress_1.pirce=600
# print(dress_1.style,dress_1.size,dress_1.pirce)
# print(dress_1.get_info())


class student :
# class property
# N=O
    #properties
    def __init__(self,name,year,scoure):
        self.name=name 
        self.year=year
        self.scour=scoure
    
    #Methods
    def get_info(self):
        print (f"name: {self.name}, year: {self.year}, scoure: {self.scoure}")
    def __str__(self):
         return f"name: {self.name} "

    
    # def add(silf.score_1):
    #    scoure= student_1

    #    scour += score_1
    #  /  return scour
    # 
    
    #   لازم يكون جوا الاسكوب بتاع classs 
#     #   واستدعيها بي self.الاسم 
    
student_1= student("Malaz", 2002,[90,95,98,96,92])
# print(student_1)
# y=0
# for i in (student_1.scour):
    # y+=i
#     sumy =sum(student.scoure)
# print(sumy)
#     avg = y / len(student_1.scour)
#     print(f" {i} \ 100\n")
# print(f"sub  = {y} \ 500")

# # # 

# class student :
#     #properties
#     y=0

#     def __init__(self,name,year,scoure):
#         self.name=name 
#         self.year=year
#         self.scour=scoure
        
    
#     #Methods
#     def get_info(self):
#         print (f"name: {self.name}, year: {self.year}, scoure: {self.scoure}")
#     def __str__(self):
#          return f"name: {self.name} "
#     def get_avereg(self) :

#         # y=0
#         # self.name ="Malaz",
#         # self.year=2002
#         # self.scour=[90,95,98,96,92]
#         # avg = y / len(self.scour)
         
#         # for i in (self.scour):
#             # y+=i

#             # avg = y / len(self.scour)
#         print(self.scour)
#             # print(f" {i} \ 100\n")
#     # print(f"scoure  = {y} \ 500\n")
#     # print(f"avg  = {avg} \ 100")
  




# class person:
#     o=0
#     name = "malaz"
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#         person.o +=1

#     def get_info(self):
#          print(f"number of person: {self.o}")

#     @classmethod
#     def get_info(cls):
#          print(f"name of person: {cls.name}")
#     def HW (self):
          
#             print(f"{self.money}")
#             return f"{self.name}"
#     def __str__ (self):
#         return f" {self.name}"
# person_1=person("me",20)
# print(person_1.get_info())  
# print(person_1.HW()) 
# print(person_1.o)  