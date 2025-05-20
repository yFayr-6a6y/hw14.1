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
        self.__products = []

        for product in products:
            self.add_product(product)

        Category.all_category += 1


    @property
    def products(self) -> str:
        """Получает строковое представление всех продуктов в категории.

        Returns:
            str: Строка с перечислением продуктов в формате "название, цена руб. Остаток: количество шт."
        """
        return "\n".join(str(product) for product in self.__products)

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

        Raises:
            TypeError: Если переданный объект не является экземпляром Product или его подклассов.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его подклассов")
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

    def average_price(self) -> float:
        """Вычисляет среднюю цену всех товаров в категории.

        Returns:
            float: Средняя цена товаров. Если товаров нет, возвращает 0.
        """
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0