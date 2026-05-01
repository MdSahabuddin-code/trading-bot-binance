def validate_side(side):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side


def validate_type(order_type):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Type must be MARKET or LIMIT")
    return order_type


def validate_qty(qty):
    qty = float(qty)
    if qty <= 0:
        raise ValueError("Quantity must be > 0")
    return qty


def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price required for LIMIT order")
        price = float(price)
        if price <= 0:
            raise ValueError("Price must be > 0")
        return price
    return None