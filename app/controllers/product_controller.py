from app.models.product import Product
from app.views.product_views import ProductViews
from app.config.database import Database

class ProductController:
    def __init__(self):
        self.product_views = ProductViews()
        self.database = Database()
        self.products = self.database.load_data()
    
    def create_products(self):
        product_data = self.product_views.get_products_data()
        new_products = Product(**product_data)
        self.products.append(new_products)
        self.database.save_data(self.products)
        self.product_views.display_message("Product created successfully.")


    def read_products(self):
        if not self.products:
            self.product_views.display_message("No products available.")
        else:
            self.product_views.display_product(self.products)
        

    def update_product(self):
        product_id  = self.product_views.get_product_id()
        product = self.find_product_by_id(product_id)
    
        if product:
            update_data = self.product_views.get_update_products_data(product)
            product.update(**update_data)
            self.database.save_data(self.products)
            self.product_views.display_message("Product updated successfully.")
        else:
            self.product_views.display_message("Product not found.")
    

    def delete_product(self):
        product_id = self.product_views.get_product_id()
        product = self.find_product_by_id(product_id)

        if product:
            self.products.remove(product) #acordate que estamos intenando hacer una persistencia
            self.database.save_data(self.products)
            self.product_views.display_message("Product deleted successfully.")
        else:
            self.product_views.display_message("Product not found.")
    
    def find_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def run(self):
        while True:
            option = self.product_views.display_menu() # Aquí estamos haciendo un menú, un crud papito

            if option == 1:
                self.create_products() 
            elif option == 2: 
                self.read_products()
            elif option == 3:
                self.update_product()
            elif option == 4:
                self.delete_product()
            elif option == 5:
                self.product_views.display_menu("Exiting the program. GoodBye!") 
                break
            else:
                self.product_views.display_message("Invalid option, Please Try again.")
                