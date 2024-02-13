from app.views.product_views import ProductViews
from app.controllers.product_controller import ProductController
from app.config.database import Database


def main():
    database = Database()
    product_controller = ProductController(database)
    product_views = ProductViews(product_controller)
    product_views.run()

if __name__ == "__main__":
    main()
