class Vars:
    def __init__(self):
        self.a = int(input("Enter the first variable: "))
        self.b = int(input("Enter the second variable: "))

    def change(self):
        self.a = int(input("Enter the first changed variable: "))
        self.b = int(input("Enter the second changed variable: "))

    def output(self):
        print(f"Your variables are {self.a}, {self.b}")

    def summa(self):
        summa = self.a + self.b
        print(f"The sum of your variables is: {summa} ")

    def largest(self):
        if self.a >= self.b:
            print(f"The largest number is {self.a}")
        else:
            print(f"The largest numbers is {self.b}")


a = Vars()
a.output()
a.summa()
a.change()
a.output()
a.largest()
