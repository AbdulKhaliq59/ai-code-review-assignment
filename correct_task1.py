def calculate_average_order_value(orders):
    valid_total = 0
    valid_count = 0

    for order in orders:
        if order["status"] != "cancelled":
            valid_total += order["amount"]
            valid_count += 1

    if valid_count == 0:
        raise ValueError("Cannot calculate average: no valid orders found")
    
    return valid_total / valid_count
