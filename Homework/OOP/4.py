class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.money = 0

    def can_add(self, v):
        return self.money + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.money += v

Box = MoneyBox(10)
Box.can_add(10)
Box.add(10)
print(Box.money)
Box.can_add(11)
Box.add(11)
print(Box.money)