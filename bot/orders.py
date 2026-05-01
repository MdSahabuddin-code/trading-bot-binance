from binance.exceptions import BinanceAPIException

def place_order(client, logger, symbol, side, order_type, qty, price=None):
    try:
        logger.info(f"REQUEST | {symbol} {side} {order_type} {qty} {price}")

        if order_type == "MARKET":
            res = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=qty
            )

        else:
            res = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=qty,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"RESPONSE | {res}")
        return res

    except BinanceAPIException as e:
        logger.error(f"API ERROR | {e}")
        raise

    except Exception as e:
        logger.error(f"GENERAL ERROR | {e}")
        raise