def insertion_sort(data_list, key, ascending=True):
    for i in range(1, len(data_list)):
        current = data_list[i]
        j = i - 1
        while j >= 0 and (
            (data_list[j][key] > current[key] if ascending else data_list[j][key] < current[key])
        ):
            data_list[j + 1] = data_list[j]
            j -= 1
        data_list[j + 1] = current
    return data_list
