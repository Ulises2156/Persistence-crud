import sqlite3
from app.models.product import Product

class Database:
    def __init__(self, db_file="product_database.db"):
        self.conn = sqlite3.connect(db_file)
        self.create_table()


    def create_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL,
                    stock INTEGER,
                    category TEXT
        ) ''')
        self.conn.commit()

    def save_data(self, products):
        c = self.conn.cursor()
        c.execute('DELETE FROM products')
        data = [(product.id, product.name, product.description, product.price, product.stock, product.category)
        for product in products]
        c.executemany('INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)',data)
        self.conn.commit()
        print("Data saved successfully")

    def load_data(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM products')
        products = [Product(*row) for row in c.fetchall()]
        print("Data loaded successfully")
        return products


    def delete_product(self, product_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM products WHERE id=?', (product_id))
        self.conn.commit()
        print("Product deleted successfully.")

    def close_connection(self):
        self.conn.close()
