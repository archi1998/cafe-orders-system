# order.py
def add_item(order, item_price):
    order.append(item_price)
    return order

def calculate_total(order):
    return sum(order)
