# class person :
#     u = 1
#     i = "malaz"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def class_info(cls):
#         return cls.u, cls.i
#     def get_info(self):
#         return f"Name: {self.name}, Age: {self.age},"
#     def __srt__(self) :
#         return f"Name: {self.name}, Age: {self.age}"
    
# person_1= person("sahar" , 22)
# person_2= person("sahar" , 22)

# person.class_info()
           

        
class doctors :
    number = 0 
    spec = [ ]

    def __init__(self, name, spec):
        self.name = name
        self.spec = spec
        doctors.number+= 1
        doctors.spec.append(spec)

    @classmethod 
    def get_spec(cls):
        return cls.spec
       
    def doctor_info( self) :
        print(f"Name: {self.name}, Spec: {self.spec}")

    def __str__(self):
            return f"Name: {self.name}, Spec: {self.spec}"
    
doctors_1 =doctors( "malaz" , "dentist")
doctors_2 =doctors( "sahar" , "oral diseases")
doctors_3 =doctors( "mona" , 3)
doctors.get_spec()
doctors_1.doctor_info()
doctors_2.doctor_info()
doctors_3.doctor_info()
# print(doctors.spec)
specs = doctors.get_spec()
for i in specs :
     print(i)


 