class ProductViews:
    def display_menu(self):
        print("\n--- Menú Product ---")
        print("1. Create Product")
        print("2. Read Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")
        return int(input("Enter you choice: "))
    


    def get_products_data(self):
        product_id = int(input("Enter Product ID: "))
        name = input ("Enter Product Name: ")
        description = input("Enter Product Description: ")
        price = float(input("Enter Product Price: "))
        stock = int(input("Enter Product Stock: "))
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
        price = float(input(f"Current Price: {product.price}, Enter New Price: ")) or product.price
        stock = int(input(f"Current Stock: {product.stock}, Enter New Stock: ")) or product. stock
        category = input(f"Current Category: {product.category}, Enter New Category: ") or product.category
        return{"name": name, "description": description, "price": price, "stock": stock, "category": category}
    
    def display_message(self, message):
        return message