from classes.Product import Product

class Category:
    """Описание категории"""

    name: str
    description: str
    products: list
    all_category: int = 0
    all_product: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        Category.all_category += 1
        Category.all_product += len(products)

    @property
    def products(self) -> str:
        count = ""
        for i in self.__products:
            count += f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт. "
        return count

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.all_product += 1

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."