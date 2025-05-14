class Product:
    """Описание продукта.

    Класс представляет продукт с его названием, описанием, ценой и количеством.
    Поддерживает операции сложения для подсчёта общей стоимости и управление ценой через свойство.
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализирует новый продукт.

        Args:
            name (str): Название продукта.
            description (str): Описание продукта.
            price (float): Цена продукта (должна быть положительной).
            quantity (int): Количество продукта на складе.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dictionary: dict) -> "Product":
        """Создаёт новый продукт из словаря.

        Args:
            dictionary (dict): Словарь с ключами, соответствующими параметрам продукта
                             (name, description, price, quantity).

        Returns:
            Product: Новый экземпляр класса Product.
        """
        return cls(**dictionary)

    @property
    def price(self) -> float:
        """Получает цену продукта.

        Returns:
            float: Текущая цена продукта.
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новую цену продукта.

        Args:
            new_price (float): Новая цена продукта.

        Notes:
            Если цена <= 0, выводится сообщение об ошибке, и цена не изменяется.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self) -> str:
        """Возвращает строковое представление продукта.

        Returns:
            str: Строка в формате "название, цена руб. Остаток: количество шт."
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Складывает общую стоимость двух продуктов одного класса.

        Args:
            other (Product): Другой продукт для сложения.

        Returns:
            float: Сумма стоимости (цена * количество) обоих продуктов.

        Raises:
            TypeError: Если other не является объектом того же класса, что и текущий объект.
        """
        if type(self) is not type(other):
            raise TypeError("Можно складывать только объекты одного класса продуктов")
        return self.__price * self.quantity + other.__price * other.quantity

class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color