from classes.Product import Product


class Category:
    """Описание категории.

    Класс представляет категорию товаров, содержащую список продуктов.
    Отслеживает общее количество категорий и продуктов.
    """

    name: str
    description: str
    products: list
    all_category: int = 0
    all_product: int = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализирует новую категорию.

        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (list): Список продуктов (объектов класса Product).
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.all_category += 1
        Category.all_product += len(products)

    @property
    def products(self) -> str:
        """Получает строковое представление всех продуктов в категории.

        Returns:
            str: Строка с перечислением продуктов в формате "название, цена руб. Остаток: количество шт."
        """
        count = ""
        for i in self.__products:
            count += f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт. "
        return count

    @products.setter
    def products(self, value: list) -> None:
        """Устанавливает список продуктов для категории.

        Args:
            value (list): Новый список продуктов (объектов класса Product).
        """
        self.__products = value

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию, если его ещё нет.

        Args:
            product (Product): Продукт для добавления.

        Notes:
            Если продукт уже присутствует, он не добавляется повторно.
            Увеличивает общее количество продуктов (all_product).
        """
        if product not in self.__products:
            self.__products.append(product)
            Category.all_product += 1

    def __str__(self) -> str:
        """Возвращает строковое представление категории.

        Returns:
            str: Строка в формате "название категории, количество продуктов: общее_количество шт."
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."