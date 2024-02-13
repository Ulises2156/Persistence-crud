import csv
from app.models.product import Product

class Database:
    def __init__(self, filename = "product_data.csv"):
        self.filename = filename
    
    def save_data(self, products):
        try:
            with open(self.filename, "w", newline="") as csvfile:
                fieldnames = ["id","name","description", "price", "stock", "category"]
                writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
                writer.writeheader()
                for product in products:
                    writer.writerow({field: getattr(product, field) for field in fieldnames})
            print("Data saved successfully")
        except Exception as e:
            print("Erro saving data:", e)

    def load_data(self):
        data = []
        try:
            with open(self.filename, "r", newline= "") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    product_data ={
                        "id": row["id"],
                        "name": row["name"],
                        "description": row["description"],
                        "price": row["price"],
                        "stock": row["stock"],
                        "category": row["category"],
                    }
                    product =Product(**product_data)
                    data.append(product)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("Erro loading data:", e)
        return data
        
