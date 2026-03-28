def validate_inputs(symbol, side, order_type, quantity, price):
    errors = []

    if not symbol or len(symbol) < 3:
        errors.append("Symbol is invalid. Example: BTCUSDT")

    if side.upper() not in ["BUY", "SELL"]:
        errors.append("Side must be BUY or SELL")

    if order_type.upper() not in ["MARKET", "LIMIT"]:
        errors.append("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        errors.append("Quantity must be greater than 0")

    if order_type.upper() == "LIMIT" and (price is None or price <= 0):
        errors.append("Price is required and must be > 0 for LIMIT orders")

    return errors