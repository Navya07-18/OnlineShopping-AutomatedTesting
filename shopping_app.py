
# Online Shopping Application

def calculate_price(price, quantity):
    if price < 0 or quantity <= 0:
        return "Invalid input"
    return price * quantity


def calculate_discount(total, discount_percentage):
    if total < 0 or discount_percentage < 0 or discount_percentage > 100:
        return "Invalid discount"
    return total - (total * discount_percentage / 100)


def calculate_cart_total(items):
    return sum(item["price"] * item["quantity"] for item in items)


def check_stock(available_stock, requested_quantity):
    if requested_quantity <= 0:
        return False
    return available_stock >= requested_quantity
