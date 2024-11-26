class Student:
    def __init__(self, name: str, age:int, address:str, marks:int):
        self.name=name 
        self.age=age 
        self.address=address
        self.marks=marks
class StudentManagementSystem:
    def __init__(self):
        self.students = []
    def add_student(self):
        name=input("Enter name: ").strip()
        while True:
            try:
                age = int(input("Enter age: "))
                break
            except ValueError:
                print("Invalid input. Age must be an integer. Please try again.")
        address=input("Enter address: ")
        while True:
            try:
                marks = int(input("Enter marks: "))
                break
            except ValueError:
                print("Invalid input. Marks must be an integer. Please try again.")
        student=Student(name,age, address, marks) 
        self.students.append(student)
        print("Student Succesfully added")
        return student
    def view_students(self):
        if len(self.students) == 0:
            print("No students found")
        else:
            view_type = input("All students or one student? (all/one): ").strip().lower()
            if view_type == "all":
                for student in self.students:
                    print(f"Name: {student.name} \n Age:{student.age}\n Address: {student.address}\n Marks : {student.marks}")
            else:
                name = input("Enter name of the student you want to see: ")
                for student in self.students:
                    if student.name == name:
                        print(f"Name: {student.name} \n Age:{student.age}\n Address: {student.address}\n Marks : {student.marks}")  
    def delete_student(self):
        name = input("Enter name of the student you want to delete: ").strip().lower()
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print("Student Succesfully deleted")
                return
        print("Kindly, Check the name and Enter correctly") 
    def update_student(self):
        name = input("Enter the student's name you want to update: ").strip()
        for student in self.students:
            if student.name == name: 
                print("Enter the choice to update") 
                while True:
                    print("1. Edit name") 
                    print("2. Edit age") 
                    print("3. Enter Address")
                    print("4. Edit marks")
                    print("Exit updating")  
                    try:
                        choice = int(input("Enter your choice: "))
                        if choice == 1:
                            student.name=input("Enter new name: ").strip()
                        elif choice == 2:
                            while True:
                                try:
                                    student.age = int(input("Enter new age: "))
                                    break
                                except ValueError:
                                    print("Invalid input. Age must be an integer.")
                        elif choice == 3:
                            student.address=input("Enter new address: ")
                        elif choice == 4:
                            while True:
                                try:
                                    student.age = int(input("Enter new marks: "))
                                    break
                                except ValueError:
                                    print("Invalid input. Age must be an integer.")
                        else:
                            print("Invalid choice. No updates were made.")
                        print("Student Succesfully updated") 
                        print(f"Name: {student.name} \n Age:{student.age}\n Address: {student.address}\n Marks : {student.marks}")
                        return 
                    except ValueError:
                        print("Invalid input. Please enter a number for your choice.")
                        return
        print("Student not found. Please check the name and try again.")
 
print("Welcome to student management system")
system =StudentManagementSystem()
while True:
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student") 
    print("4. View Student")    
    print("5. Exit the system")    
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            system.add_student()
        elif choice == 2:
            system.delete_student()
        elif choice == 3:
            system.update_student()
        elif choice == 4:
            system.view_students()
        elif choice == 5:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")
                   