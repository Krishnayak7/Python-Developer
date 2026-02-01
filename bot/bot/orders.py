import logging
from .validators import validate_inputs

logger = logging.getLogger(__name__)

def place_trade(client, symbol, side, order_type, quantity, price=None):
    validate_inputs(symbol, side, order_type, quantity, price)

    order_data = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        order_data.update({
            "price": price,
            "timeInForce": "GTC"
        })

    logger.info(f"Placing order: {order_data}")
    return client.place_order(**order_data)
