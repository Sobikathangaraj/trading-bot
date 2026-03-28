from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(client, symbol, side, order_type, quantity, price=None):
    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity,
    }

    if order_type.upper() == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    logger.info(f"Placing {order_type} {side} order for {quantity} {symbol}")
    return client.place_order(**params)