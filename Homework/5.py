class InternetShop:
    def __init__(self, name):
        self.name = name

    stock = []

    class Seller:

        def __init__(self, name):
            self.name = name

        def add_info(self, product):
            InternetShop.stock.append(product)

        def check_storage(self):
            if self in Storage.storage:
                print("На складе присутствует товар, ожидайте доставку в магазин")
                InternetShop.stock.append(self)
            else:
                print("К сожалению товар отсутствует и на складе")

        def check(self):
            if self in InternetShop.stock:
                print("Товар в магазине присутствует")
                print(f"Вы приобрели {self}")
            else:
                print("Товар отсутствует в магазине")
                InternetShop.Seller.check_storage(self)

    class Product:
        def __init__(self, name):
            self.name = name

    class Client:
        def __init__(self, name):
            self.name = name

        def buy(self, name):
            print(f"Вы создали заявку на товар {name}")
            InternetShop.Seller.check(name)


class Storage(InternetShop):
    storage = ["Nike", "Puma"]


Sneakers_shop = InternetShop("Sneakers.by")
Rick = InternetShop.Seller("Rick")
Mike = InternetShop.Client("Mike")
Rick.add_info("Adidas")
Mike.buy("Adidas")
Michael = InternetShop.Client("Michael")
Michael.buy("Nike")
Mike.buy("Lacoste")
