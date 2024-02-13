class ProductViews:
    def __init__(self, product_controller):
        self.product_controller = product_controller

    def run(self):
        while True:
            option = self.display_menu()

            if option == 1:
                product_data = self.get_product_data()
                if product_data:
                    self.product_controller.create_product(product_data)
            elif option == 2:
                products = self.product_controller.read_products()
                self.display_products(products)
            elif option == 3:
                product_id = self.get_product_id()
                update_data = self.get_update_data()
                self.product_controller.update_product(product_id, update_data)
                pass
            elif option == 4:
                product_id = self.get_product_id()
                self.product_controller.delete_product(product_id)
                pass
            elif option == 5:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def display_menu(self):
        print("\n--- Menu ---")
        print("1. Create Product")
        print("2. Read Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        return int(input("Enter your choice: "))

    def get_product_data(self):
        while True:
            try:
                product_id = int(input("Enter Product ID: "))
                if self.product_controller.find_product_by_id(product_id):
                    print("Product with this ID already exits. Please choose another ID.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid numeric ID.")
        name = input("Enter Product Name: ")
        description = input("Enter Product Description: ")

        while True:
            try:
                price = float(input("Enter Product Price: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid numeric price.")
        
        stock = int(input("Enter Product Stock: "))
        category = input("Enter Product Category: ")
        return {"id": product_id, "name": name, "description": description, "price": price, "stock": stock, "category": category}
    pass

    def display_products(self, products):
        if not products:
            print("No products available.")
        else:
            print("\n---- Product List ----")
        for product in products:
            print(product)

    def get_product_id(self):
        return int(input("Enter Product ID: "))

    def get_update_data(self):
        print("\nEnter new data for the product (press Enter to keep the current value):")
        name = input("Enter New Name: ")
        description = input("Enter New Description: ")
        price = input("Enter New Price: ")
        stock = input("Enter New Stock: ")
        category = input("Enter New Category: ")
        return {"name": name, "description": description, "price": price, "stock": stock, "category": category}

