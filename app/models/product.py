import csv

class Product:
    def __init__(self, id, name, description, price, stock, category):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: {self.price}, Stock: {self.stock}, Category: {self.category} "

    def load_all(filename="product:data.csv"):
        products = []
        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    product = Product(
                        row["id"],
                        row["name"],
                        row["description"],
                        row["price"],
                        row["stock"],
                        row["category"]
                    )
                    products.append(product)
        except FileNotFoundError:
            pass
        return products
    def save(self, filename="product_data.csv"):
        with open(filename, "a", newline="") as csvfile:
            filenames = ["id", "name", "description", "price", "stock", "category"]
            writer = csv.DictWriter(csvfile, fieldnames=filenames)

            writer.writerow({
                "id": self.id,
                "name":self.name,
                "description": self.description,
                "price": self.price,
                "stock": self.stock,
                "category": self.category
            })
