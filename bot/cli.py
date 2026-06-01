import argparse

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    side = validate_side(args.side)

    order_type = validate_order_type(args.type)

    quantity = validate_quantity(args.quantity)

    price = validate_price(args.price, order_type)

    return {
        "symbol": args.symbol,
        "side": side,
        "order_type": order_type,
        "quantity": quantity,
        "price": price
    }