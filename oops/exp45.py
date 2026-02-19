class Student:
    school_name="abc"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
obj=Student(name="Abi",roll_no=1010)
print(obj.school_name)
print(obj.name)
print(obj.roll_no)
obj.school_name="Rec"
print(obj.school_name)
print(obj.name)
print(obj.roll_no)