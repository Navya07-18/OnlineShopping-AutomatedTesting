
from shopping_app import (
    calculate_price,
    calculate_discount,
    calculate_cart_total,
    check_stock
)


def test_calculate_price():
    assert calculate_price(500, 2) == 1000


def test_invalid_price():
    assert calculate_price(-100, 2) == "Invalid input"


def test_calculate_discount():
    assert calculate_discount(1000, 10) == 900


def test_invalid_discount():
    assert calculate_discount(1000, 120) == "Invalid discount"


def test_calculate_cart_total():
    items = [
        {"price": 500, "quantity": 2},
        {"price": 300, "quantity": 1}
    ]
    assert calculate_cart_total(items) == 1300


def test_check_stock_available():
    assert check_stock(10, 5) is True


def test_check_stock_unavailable():
    assert check_stock(3, 5) is False


def test_invalid_stock_quantity():
    assert check_stock(10, 0) is False
