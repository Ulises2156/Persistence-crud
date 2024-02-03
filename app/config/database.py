import csv

class Database:
    def __init__(self, filename = "product_data.csv"):
        self.filename = filename
    
    def save_data(self, data):
        with open(self.filename, "w", newline="") as csvfile:
            fieldnames = ["id","name","description", "price", "stock", "category"]
            writer = csv.DictWriter(csvfile, fieldnames= fieldnames)

            writer.writeheader()
            for product in data:
                writer.writerow(product.__dict__)
    
    def load_data(self):
        data = []
        try:
            with open(self.filename, "r", newline= "") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            pass
        return data
    