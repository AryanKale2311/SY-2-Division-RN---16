class student_report:
    def decorator(func):
        def wrapper(self,name,attendance,rollno,division):
            print ("="*40)
            print("              REPORT")
            print ("="*40)
            func(self,name,attendance,rollno,division)
            print ("="*40)
            print("              END")
            print ("="*40)
        return wrapper
    
    @decorator
    def student_name(self,name,attendance,rollno,division):
        self.name = name
        self.rollno = rollno
        self.attendance = attendance 
        self.division = division
        print (f"Hello {name}.")
        print(f"The {name} has {attendance}% attendance .")
        print (f"The {name} has {rollno} as his roll number.")
        print (f"The {name} is in SY {division} division.")

student = student_report()
student.student_name(str(input("Enter Student name : ")),int(input("Enter Student attendance : ")),int(input("Enter Student Roll number : ")),int(input("Enter Student Division : ")))
    