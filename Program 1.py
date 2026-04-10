#Program I chose was from the Object-oriented Programming (OOP) video by programiz first video from this week. I changed a bit of it though

class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def check_pass_fail(self):
        if self.mark >= 60:
            return "Pass"
        else:
            return "Fail"

student1 = Student("Mario", 75)
student2 = Student("Luigi", 86)
student3 = Student("Toad", 95)
student4 = Student("Bowser", 45)

did_pass = student1.check_pass_fail()
print(f"{student1.name} has a mark of {student1.mark} and has {did_pass}.")

did_pass = student2.check_pass_fail()
print(f"{student2.name} has a mark of {student2.mark} and has {did_pass}.")

did_pass = student3.check_pass_fail()
print(f"{student3.name} has a mark of {student3.mark} and has {did_pass}.")

did_pass = student4.check_pass_fail()
print(f"{student4.name} has a mark of {student4.mark} and has {did_pass}.")
