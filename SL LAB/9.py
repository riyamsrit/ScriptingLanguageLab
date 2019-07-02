class Student :
    Name=""
    age=0
    sublist=[]

    def __init__(self,x,y,l):
        self.Name=x
        self.age=y
        self.sublist=l 
    def accept(self):
        self.Name=input("Enter the name")
        self.age=input("Enter the age")
        print("Enter the marks of students")
        l=input()
        l=l.split(" ")
        x=[]
        for i in range (len(l)):
            x.append(int(l[i]))
        self.sublist=x
    def disp(self):
         print(self.Name)
         print(self.age)
         print(self.sublist)

s1=Student('Ri',25,[45,33,65,86])
s1.disp()

s2=Student('Si',33,[65,44,22,11])
s2.disp()
s2.accept()
s2.disp()