from app.models.product import Product

class ProductController:
    def __init__(self, database):
        self.database = database
        self.products = self.database.load_data()

    def create_product(self, product_data):
        existing_ids =[product.id for product in self.products]
        if product_data["id"] in existing_ids:
            print("Product with this ID already exists. Please choose another ID. ")
        else:
            new_product = Product(**product_data)
            new_product.save_to_database(self.database.conn)
            self.products.append(new_product)
            print("Product created succcessfully.")

    def read_products(self):
        return self.products

    def update_product(self, product_id, update_data):
        product = self.find_product_by_id(product_id)
        if product:
                for key, value in update_data.items():
                    setattr(product, key, value)
                print("Product updated successfully.")
                product.save_to_database(self.database.conn)

    def delete_product(self, product_id):
        product = self.find_product_by_id(product_id)
        if product:
            self.products.remove(product)
            product.delete_from_database(self.database.conn)
            print("Product deleted successfully.")
        else:
            print("Product not found")

    def find_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

