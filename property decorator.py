class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
 
stu1=student(99,98,77)
print(stu1.percentage)

stu1.phy=70
print(stu1.percentage)

class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def percentage(self):
        return str((self.phy+self.math+self.chem)/3)+"%"

stu1=student(99,98,97)
print(stu1.percentage)

stu1.phy=20
print(stu1.percentage)