class Product:
    def __init__(self, product_id, name, description, price, stock, category):
        self.id= product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: {self.price}, Stock: {self.stock}, Category: {self.category}"
