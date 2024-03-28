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

    def save_to_database(self, conn):
        c = conn.cursor()
        c.execute("SELECT * FROM products WHERE id=?", (self.id,))
        existing_product = c.fetchone()

        if existing_product:
            c.execute("""
                UPDATE products
                SET name=?, description=?, price=?, stock=?, category=?
                WHERE id=?
            """, (self.name, self.description, self.price, self.stock, self.category, self.id))
        else:
            c.execute("""
                INSERT INTO products (id, name, description, price, stock, category)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (self.id, self.name, self.description, self.price, self.stock, self.category))

        conn.commit()

    def delete_from_database(self, conn):
        c = conn.cursor()
        c.execute("DELETE FROM products WHERE id=?",(self.id,))
        conn.commit()
