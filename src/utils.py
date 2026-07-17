def format_currency(value):

    if value >= 1_000_000:
        return f"${value/1_000_000:.2f} M"

    elif value >= 1000:
        return f"${value/1000:.2f} K"

    else:
        return f"${value:.2f}"