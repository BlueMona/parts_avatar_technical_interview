# Task: Error Handling & Resilience
# Goal: Calculate a discount safely.

def calculate_discount(price, discount_percent):
    """
    Instructions: Handle cases where discount_percent is 0 
    or if inputs are strings/None. Return 0 for invalid inputs.
    """
    # TODO: Implement logic
    if price is not None and discount_percent is not None:
        if price == 0 or discount_percent == 0: 
            return 0
        else: 
            discount_amount = float(price)*float(discount_percent)*(0.01)
            return discount_amount
    else: 
        return 0
    

# Test Case
print(calculate_discount(100, "10")) # Should return 0 or handle conversion
print(calculate_discount(100, 0))    # Should return 0
print(calculate_discount(None, 10))