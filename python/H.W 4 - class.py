
class School:
   
    def __init__(self, names, class_name, grades):
        self.names = names  
        self.class_name = class_name  
        self.grades = grades  

    def num(self):
        return f"Number of students in {self.class_name}: {len(self.names)}"

    def calculate_gpa(self):
        total_gpa = 0  
        for grades in self.grades:
            student_avg = sum(grades) / len(grades)  
            total_gpa += student_avg  
        
        class_avg = total_gpa / len(self.grades) 
        return class_avg

    def print_students_info(self):
        print(f"\n{self.class_name} Students:")
        for i in range(len(self.names)):
            student_avg = sum(self.grades[i]) / len(self.grades[i])  
            print(f"Name: {self.names[i]} | GPA: {student_avg:.2f} | Class: {self.class_name}")


Name_of_class_1 = ["Amal", "Suha", "Amani"]
Name_of_class_2 = ["Rowa", "Alaa", "Salma"]
Name_of_class_3 = ["Mohamed", "Ahmed", "Amar"]
Name_of_class_4 = ["Yasein", "Mazin", "Amjed"]

Grades_1 = [[91, 93, 89], [89, 70, 85], [89, 98, 90]]
Grades_2 = [[89, 85, 90], [90, 98, 95], [84, 95, 89]]
Grades_3 = [[87, 83, 90], [94, 89, 79], [82, 95, 84]]
Grades_4 = [[85, 90, 89], [90, 95,92], [89, 85, 90]]

class_1 = School(Name_of_class_1, "Class 1", Grades_1)
class_2 = School(Name_of_class_2, "Class 2", Grades_2)
class_3 = School(Name_of_class_3, "Class 3", Grades_3)
class_4 = School(Name_of_class_4, "Class 4", Grades_4)

print(class_1.num())
print(class_2.num())
print(class_3.num())
print(class_4.num())

class_1.print_students_info()
class_2.print_students_info()
class_3.print_students_info()
class_4.print_students_info()
