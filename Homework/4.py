class MoneyBox:
    money = 0

    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        if MoneyBox.money + v <= self.capacity:
            print("Вмещается")
        else:
            print("Не вмещается")

    def add(self, v):
        if MoneyBox.money + v <= self.capacity:
            MoneyBox.money += v
            print(f"Ваш баланс {MoneyBox.money}")
        else:
            print(f"Превышен лимит, ваш текущий баланс {MoneyBox.money} ")




Box = MoneyBox(10)
Box.can_add(10)
Box.add(5)
Box.add(5)
Box.add(5)
