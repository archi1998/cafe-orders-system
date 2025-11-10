# tests/test_order.py
from src.order import add_item, calculate_total

def test_add_item():
    order = []
    add_item(order, 10)
    assert order == [10]

def test_calculate_total():
    order = [5, 15]
    total = calculate_total(order)
    assert total == 20
