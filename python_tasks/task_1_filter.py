# Task: List Comprehension & Filtering
# Instructions: Complete the function to return only even IDs 
# greater than 100, sorted in descending order.

def is_even_and_greater_than_100(number):
    if (number % 2 == 0) and (number > 100):
        return True
    else: 
        return False


def filter_orders(order_ids):
    # TODO: Write your logic here
    filtered = filter(is_even_and_greater_than_100, test_data)

    return sorted(filtered)

# Test Case
test_data = [10, 105, 120, 44, 202, 300, 75, 110]
# Expected Output: [300, 202, 120, 110]
print(filter_orders(test_data))