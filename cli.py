import argparse
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logger


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()
    logger = setup_logger()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_type(args.type)
        qty = validate_qty(args.quantity)
        price = validate_price(args.price, order_type)

        client = BinanceClient().get()

        print("\n--- ORDER REQUEST ---")
        print(symbol, side, order_type, qty, price)

        res = place_order(
            client, logger, symbol, side, order_type, qty, price
        )

        order_id = res.get("orderId")

        # ✅ Fetch latest order status (FIXED INDENTATION)
        final = client.futures_get_order(
            symbol=symbol,
            orderId=order_id
        )

        print("\n--- ORDER SUCCESS ---")
        print(f"Order ID: {order_id}")
        print(f"Status: {final.get('status')}")
        print(f"Executed Qty: {final.get('executedQty')}")
        print(f"Avg Price: {final.get('avgPrice', 'N/A')}")

    except Exception as e:
        print("\n--- ORDER FAILED ---")
        print(str(e))


if __name__ == "__main__":
    main()