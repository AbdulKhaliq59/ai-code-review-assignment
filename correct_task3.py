def average_valid_measurements(values):
    total = 0
    valid_count = 0

    for v in values:
        if v is not None:
            total += float(v)
            valid_count += 1

    if valid_count == 0:
        raise ValueError("Cannot calculate average: no valid measurements found")
    
    return total / valid_count
