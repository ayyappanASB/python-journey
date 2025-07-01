class marklist:
    def __init__(self,name,tam,eng,mat,total,aver,res):
        self.name=name
        self.tam=tam
        self.eng=eng
        self.mat=mat
    def get(self):
        self.name=input("enter your name")
        self.tam=int(input("Enter tamil mark:"))
        self.eng=int(input("enter english mark"))
        self.mat=int(input("Enter mat mark"))
    def calc(self):
        self.total=self.tam+self.eng+self.mat
        self.aver=self.total/3
        if(self.tam>=40 and self.eng>=40 and self.mat>=40):
            self.res="pass"
        else:
            self.res="fail"
    def printall(self):
        print("Name:",self.name)
        print("Tamil mark:",self.tam)
        print("English mark:",self.eng)
        print("Maths mark:",self.mat)
        print("Total:",self.total)
        print("Average:",self.aver)
        print("Result:",self.res)
print("OBJECT 1")
ob1=marklist('vijay',40,40,40,120,40,'pass')
ob1.get()
ob1.calc()
ob1.printall()

print("-------"*10)
print("OBJECT 2")
ob2=marklist('vijay',50,50,50,150,50,'pass')
ob2.get()
ob2.calc()
ob2.printall()

                 