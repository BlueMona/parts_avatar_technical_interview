# Task: String Formatting
# Goal: Transform a raw SKU into a readable title.

def format_sku(sku_string):
    """
    Instructions: Convert 'engine-oil-10w30' to 'Engine Oil 10w30'.
    """
    # TODO: Implement logic
    answer_string = sku_string.replace("-", " ")

    return answer_string

# Test: format_sku("brake-pads-ceramic") -> "Brake Pads Ceramic"

format_sku("barke-pads-ceramic")