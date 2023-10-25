"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def product2():
    return Product("apple", 50, "This is an apple", 300)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product, product2):
        # TODO напишите проверки на метод check_quantity
        assert Product.check_quantity(product, 999)
        assert Product.check_quantity(product, 1000)
        assert Product.check_quantity(product2, 200)
        assert not Product.check_quantity(product, 1001)

    def test_product_buy(self, product, product2):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 900

        with pytest.raises(ValueError):
            product2.buy(500)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError, match='Запрашиваемого продукта нет в таком количестве'):
            Product.buy(product, 12000)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, product, product2, cart):
        """
        Проверки на метод add_product
        """
        cart.add_product(product, 1)
        assert cart.products[product] == 1

        cart.add_product(product2, 3)
        assert cart.products[product2] == 3

        cart.add_product(product, 2)
        with pytest.raises(AssertionError):
            assert cart.products[product] == 4

    def test_cart_remove_product(self, product, product2, cart):
        """
        Проверки на метод remove_product
        """
        cart.add_product(product, 4)
        cart.remove_product(product, 3)
        assert cart.products[product] == 1

        with pytest.raises(ValueError):
            assert cart.remove_product(product2)


    def test_cart_clear(self, product, product2, cart):
        """
        Проверки на метод clear
        """
        cart.add_product(product, 4)
        cart.add_product(product2, 1)
        cart.add_product(product, 3)
        assert cart.clear() == {}


    def test_cart_get_total_price(self, product, product2, cart):
        """
        Проверки на метод get_total_price
        """
        cart.add_product(product, 4)
        cart.add_product(product2, 1)
        cart.add_product(product, 3)
        assert cart.get_total_price() == 750.0


    def test_cart_buy(self, product, product2, cart):
        """
        Проверки на метод buy
        """

        cart.add_product(product2, 10)
        cart.buy()
        assert product2.quantity == 290

        with pytest.raises(ValueError):
            cart.add_product(product, 5000)
            cart.buy()



