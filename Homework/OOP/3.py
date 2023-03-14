class Shop:
    catalog = []


    def __init__(self, name):
        self.name = name
        Shop.catalog.append(self.name)
        print(f"{self.name} is added")

    def remove(self):
        Shop.catalog.remove(self)
        print(f"{self} is deleted")

    def searching(self):
        if self in Shop.catalog:
            print(f"{self} in stock")
        else:
            print(f"{self} is absent")


Meat = Shop("Meat")
Fish = Shop("Fish")
Milk = Shop("Milk")
print(Shop.catalog)
Shop.searching("Milk")
Shop.remove("Milk")
Shop.searching("Milk")
print(Shop.catalog)
