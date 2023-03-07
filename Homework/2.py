class Counter:
    def __init__(self):
        self.s = 1
        self.e = 10
        self.my_counter = 5

    def input(self):
        self.s = int(input("Enter the starting number of the range: "))
        self.e = int(input("Enter the end number of the range: "))
        self.my_counter = int(input("Enter counter value: "))

    def range(self):
        my_range = []
        for element in range(self.s, self.e + 1):
            my_range.append(element)
        number = my_range.index(self.my_counter)
        print(f"The current counter is above the number {number} in your range {my_range}")

    def plus(self):
        self.my_counter += 1

    def minus(self):
        self.my_counter = self.my_counter - 1

    def current(self):
        print(f"The current counter is {self.my_counter}")


a = Counter()
a.input()
a.current()
a.range()
a.plus()
a.current()
a.range()
