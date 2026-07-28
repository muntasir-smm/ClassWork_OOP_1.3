from datetime import date

class Product:
    def __init__(self, name, batch_no, price, category, mfd):
        self.name = name
        self.batch_no = batch_no
        self.price = price
        self.category = category
        self.mfd = mfd

    def product_info(self):
        print(f"Product Name : {self.name}")
        print(f"Batch No     : {self.batch_no}")
        print(f"Price        : ৳ {self.price}")
        print(f"Category     : {self.category}")
        print(f"Manufacture Date : {self.mfd}")


class Buyer:
    def __init__(self, name, address, phone, order_count):
        self.name = name
        self.address = address
        self.phone = phone
        self.order_count = order_count

    def buyer_info(self):
        print(f"Buyer Name : {self.name}")
        print(f"Address    : {self.address}")
        print(f"Phone      : {self.phone}")


class Seller:
    def __init__(self, name, address, phone, sell_count):
        self.name = name
        self.address = address
        self.phone = phone
        self.sell_count = sell_count

    def seller_info(self):
        print(f"Seller Name : {self.name}")
        print(f"Address     : {self.address}")
        print(f"Phone       : {self.phone}")


class Purchase:
    def __init__(self, product, buyer, seller, quantity):
        self.product = product
        self.buyer = buyer
        self.seller = seller
        self.quantity = quantity

    def purchase_info(self):
        total = self.product.price * self.quantity

        print(f"\nPurchase Information:\nProduct : {self.product.name} \nBuyer   : {self.buyer.name}\nSeller  : {self.seller.name}\nQuantity: {self.quantity}\nTotal Price: ৳ {total}")


def main():
    product1 = Product("Honey Bread", 319, 10, "Food", date(2026, 6, 15))
    buyer1 = Buyer("Munna", "Ashulia, Dhaka", "0123456", 10)
    seller1 = Seller("ABC Store", "Ashulia, Dhaka", "01712345678", 100)

    product1.product_info()
    print()

    buyer1.buyer_info()
    print()

    seller1.seller_info()

    purchase1 = Purchase(product1, buyer1, seller1, 5)
    purchase1.purchase_info()

main()