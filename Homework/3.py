class Shop:
    catalog = []

    def __init__(self, name):
        self.name = name

    class Product:
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


My_shop = Shop("My shop")
Fish = Shop.Product("Fish")
Milk = Shop.Product("Milk")
print(Shop.catalog)
Shop.Product.searching("Milk")
Shop.Product.remove("Milk")
Shop.Product.searching("Milk")
print(Shop.catalog)
