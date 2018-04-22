

def mean(datasets):
    avg = 0
    for item in datasets:
        avg += item
    return avg/len(datasets)


def median(datasets):
    datasets.sort()
    if (len(datasets) % 2) == 0:
        first_data = datasets[int((len(datasets)/2)) - 1]
        second_data = datasets[int((len(datasets)+2)/2) - 1]
        return (first_data + second_data) / 2
    else:
        return datasets[int((len(datasets) + 1)/2) - 1]


def mode(list_in):
    count_dict = {}
    for e in list_in:
        count = list_in.count(e)
        if e not in count_dict.keys():
            count_dict[e] = count
    max_count = 0
    for key in count_dict:
        if count_dict[key] >= max_count:
            max_count = count_dict[key]
    corr_keys = []
    for corr_key, count_value in count_dict.items():
        if count_dict[corr_key] == max_count:
            corr_keys.append(corr_key)
    if max_count == 1 and len(count_dict) != 1:
        return 'No mode for this dataset. All values occur only once.'
    else:
        corr_keys = sorted(corr_keys)
        return corr_keys, max_count


array = [10, 30, 20, 40, 50, 10, 2, 2]
print("DATASETS:", array)
print("MEAN:", mean(array))
print("MEDIAN:", median(array))
[x, y] = mode(array)
print("MODE:", x)
