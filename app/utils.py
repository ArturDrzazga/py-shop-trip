def format_price(price: float) -> str:
    if price.is_integer():
        return str(int(price))
    else:
        return ("{:.2f}".format(price)).rstrip("0").rstrip(".")
