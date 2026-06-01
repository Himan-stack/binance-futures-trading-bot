from bot.client import BinanceClient
from bot.logging_config import logger

client = BinanceClient()


def execute_order(symbol, side, order_type, quantity, price=None):

    try:

        logger.info(
            f"Order Request -> "
            f"Symbol: {symbol}, "
            f"Side: {side}, "
            f"Type: {order_type}, "
            f"Quantity: {quantity}, "
            f"Price: {price}"
        )

        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        logger.info(f"API Response -> {response}")

        return response

    except Exception as e:

        logger.error(f"Order Execution Error -> {str(e)}")

        return {
            "error": str(e)
        }