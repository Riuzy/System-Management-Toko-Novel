def binary_search(data_list, key, value):
    low = 0
    high = len(data_list) - 1
    value = value.strip().lower()

    while low <= high:
        mid = (low + high) // 2
        mid_value = str(data_list[mid].get(key, "")).strip().lower()

        if mid_value == value:
            return data_list[mid]
        elif mid_value < value:
            low = mid + 1
        else:
            high = mid - 1

    return None
