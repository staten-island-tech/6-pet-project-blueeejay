# intro to inheritance:
#PARENT CLASS.. it's children will have simlar attributes. AKA BASE OR SUPER 
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    # child class = derived, subclass... can "extend or override {parent} behavior"
class Student(User):
     def __init__(self, name, email, student_id):
        super().__init__(name, email)  # Call the parent class constructor
        self.student_id = student_id
    
     def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
     # CHILD 1 

class Teacher(User):
      def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
      def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"
    # CHILD 2 

class Administrator(User):
     def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
     def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
     # CHIlD 3 
student = Student("Alice", "alice@example.com", "S12345")
teacher = Teacher("Mr. Smith", "smith@example.com", "Mathematics")
administrator = Administrator("Ms. Johnson", "johnson@example.com", "Principal")

print(student.display_info())
print(teacher.display_info())
print(administrator.display_info())
# OVERRIDING PARENT 