from abc import ABC, abstractmethod

class ReprLoggingMixin:
    """
    Миксин для логирования создания объектов и представления
    Реализует магический метод __repr__ и расширяет __init__
    """

    def __init__(self, *args, **kwargs):
        """
        Расширяет конструктор базового класса логированием параметров создания
        """
        print(f"Создание объекта {self.__class__.__name__} с параметрами:")
        for name, value in kwargs.items():
            print(f"  {name}: {value}")

        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        """
        Стандартное представление объекта для разработчика
        Формат: <ClassName(arg1=value1, arg2=value2)>
        """
        args_str = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"<{self.__class__.__name__}({args_str})>"


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(BaseProduct, ReprLoggingMixin):
    """Класс продукта с наследованием от BaseProduct и миксина"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(
            name=name,
            description=description,
            price=price,
            quantity=quantity
        )

    def __str__(self) -> str:
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."


    @property
    def price(self) -> float:
        """Получает цену продукта.

        Returns:
            float: Текущая цена продукта.
        """
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новую цену продукта.

        Args:
            new_price (float): Новая цена продукта.

        Raises:
            ValueError: Если цена нулевая или отрицательная.
        """
        if new_price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self._price = new_price


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
        return self._price * self.quantity + other._price * other.quantity

    @classmethod
    def new_product(cls, dictionary: dict) -> "Product":
        return cls(**dictionary)

class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(
            name=name,
            description=description,
            price=price,
            quantity=quantity
        )
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str):
        super().__init__(
            name=name,
            description=description,
            price=price,
            quantity=quantity
        )
        self.country = country
        self.germination_period = germination_period
        self.color = color