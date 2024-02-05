import csv
from app.models.product import Product

class Database:
    def __init__(self, filename = "product_data.csv"):
        self.filename = filename
    
    def save_data(self, products):
        with open(self.filename, "w", newline="") as csvfile:
            fieldnames = ["id","name","description", "price", "stock", "category"]
            writer = csv.DictWriter(csvfile, fieldnames= fieldnames)

            writer.writeheader()
            for product in products:
                writer.writerow({field: getattr(product, field) for field in fieldnames})
    
    def load_data(self):
        data = []
        try:
            with open(self.filename, "r", newline= "") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    product_data ={
                        "product_id": row["id"],
                        "name": row["name"],
                        "description": row["description"],
                        "price": row["price"],
                        "stock": row["stock"],
                        "category": row["category"],
                    }
                    product =Product(**product_data)
                    data.append(product)
        except FileNotFoundError:
            pass
        return data
    
    
