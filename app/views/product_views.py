class ProductViews:
    def display_menu(self, exit_message=None):
        print("\n--- Menú Product ---")
        print("1. Create Product")
        print("2. Read Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")
        if exit_message:
            print(exit_message)

        return int(input("Enter you choice: "))

    def get_products_data(self, existing_ids):
        while True:
            try:
                product_id = int(input("Enter Product ID: "))
                if product_id in existing_ids:
                    print("Product with this ID already exits. Please choose another ID.")
                else:
                    break
            except ValueError: # estamos probrando un try y except, porque sigue saliendo error en id
                print("Invalid input. Please enter a valid numeric ID.")

        name = input ("Enter Product Name: ")
        description = input("Enter Product Description: ")

        while True:
            try:
                price = float(input("Enter Product Price: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid numeric price")
        while True:
            try:
                stock = int(input("Enter Product Stock: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid numeric stock")
        category = input("Enter Product Category: ")
        return {"product_id": product_id, 
                "name": name, 
                "description": description,
                "price": price,
                "stock": stock, 
                "category": category }

    def display_product(self, products):
        print("\n---- Product List ----")
        for product in products:
            print(product)

    def get_product_id(self):
        return int(input("Enter Product ID: "))

    def get_update_products_data(self, product):
        print("\n Enter new for the product (press Enter to kepp the current value):")
        name = input(f"Current Name: {product.name}, Enter New Name: ") or product.name
        description = input(f"Current Description: {product.description}, Enter New Description: ") or product.description
        price = input(f"Current Price: {product.price}, Enter New Price: ") or product.price
        stock = input(f"Current Stock: {product.stock}, Enter New Stock: ") or product. stock
        category = input(f"Current Category: {product.category}, Enter New Category: ") or product.category
        
        update_data = {
            "name": name,
            "description": description,
            "price": price,
            "stock": stock,
            "category": category
        }
        return update_data
    
    def display_message(self, message):
        return message
