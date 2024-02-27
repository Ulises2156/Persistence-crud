import csv
from app.models.product import Product

class Database:
    def __init__(self, filename="product_data.csv"):
        self.filename = filename
    
    def save_data(self, products):
        try:
            with open(self.filename, "w", newline="") as csvfile:
                fieldnames = ["id", "name", "description", "price", "stock", "category"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for product in products:
                    writer.writerow({field: getattr(product, field) for field in fieldnames})
            print("Data saved successfully")
        except Exception as e:
            print("Error saving data:", e)

    def load_data(self):
        data = []
        try:
            with open(self.filename, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    product_data = {
                        "id": row["id"],
                        "name": row["name"],
                        "description": row["description"],
                        "price": row["price"],
                        "stock": row["stock"],
                        "category": row["category"],
                    }
                    product = Product(**product_data)
                    data.append(product)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("Error loading data:", e)
        return data
    
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
    
    def save(self, products, filename="product_data.csv"):
        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["id", "name", "description", "price", "stock", "category"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for product in products:
                writer.writerow({field: getattr(product, field) for field in fieldnames})
            print("Data saved successfully")
    
    def delete_product(self, product_id):
        products = self.load_data()
        updated_products = [product for product in products if product.id != product_id]
        self.save_data(updated_products)
        print("Product deleted successfully.")
