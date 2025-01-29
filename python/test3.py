
class school :
    Class_1_GPA= [ ]  
    Class_2_GPA= [ ]  
    Class_3_GPA= [ ]  

    r = 0
    e = 0
    u = 0
 

    def __init__ (self,Name,Class_,Grades) :
        self.Name = Name 
        self.Class_ = Class_
        self.Grades = Grades


        for i in self.Grades [0] :
            print("",end="")
            school.r +=i 
          
        school.Class_1_GPA.append(school.r)
       

        for o in (self.Grades[1]) :
            school.e +=o
            GBA2 = o / (len(self.Grades[1]))

        school.Class_2_GPA.append(GBA2)
        
        for p in (self.Grades[2]) :
            school.u +=p
            GBA3 = p / (len(self.Grades[2]))
        school.Class_2_GPA.append(GBA3)

    def school_info(self):
        print(f"Name :{self.Name},Class {self.Class_} ,Grades {self.Grades}")
    def __str__ (self):
            return f"Name :{self.Name}"
    def num(self) :
        return f"number of class 1 :{len(self.Name)}"
    def num2(self) :
        return f"number of class 2 :{len(self.Name)}"
    def num3(self) :
        return f"number of class 3 :{len(self.Name)}"
    

    def calculate_gpa(self):
        student_averages = [sum(grade) / len(grade) for grade in self.grades]  
        class_avg = sum(student_averages) / len(student_averages)  
        return class_avg
        

class_1 = school(["Malaz" , "Sahar" , "Walaa" ],"class 1" ,[[91,93,89],[89,70,85] ,[79,98,90]])
class_2 = school(["Mona " , "fatima" , "Mina" ],"class 2" ,[[69,85,90],[90,98,95],[74,69.89] ])
class_3 = school(["Mohamed" , "Ahmed" , "omer" ],"class 3" ,[[87,83 ,90],[94,89,79],[82,95,84]])


print(class_1.num())
print(class_2.num2())
print(class_3.num3())
