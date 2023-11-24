class Product:

    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price

    def __str__(self):
        return self.type + "," + self.name + "," + str(self.price)


class ProductStore:
    earning = 0

    def __init__(self):
        self.earning = 0
        self.products = dict()

    def add(self, product, amount):
        self.products[product.name] = {
            "type": product.type,
            "price": product.price * 1.3,
            "amount": amount
        }

        return self.products[product.name]

    def set_discount(self, identifier, percent, identifier_type='name'):
        for product, amount in self.products.items():
            if product.type_product == identifier_type or product.name == identifier:
                product.price *= (1 - percent / 100)

            print("There is no such product")

    def sell_product(self, product_name, amount):
        if product_name in self.products:
            if self.products[product_name]['amount'] >= amount:
                self.products[product_name]['amount'] -= amount
                self.earning += amount * self.products[product_name]["price"]
            else:
                raise ValueError(f"there is not enough goods: {self.products[product_name]}")
        else:
            raise ValueError("Not found")

    def get_income(self):
        return self.earning

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        if product_name in self.products:
            return product_name, self.products[product_name]["amount"]

        else:
            raise ValueError(f"{product_name} not found")


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)
print(s.products)
