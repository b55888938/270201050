def get_reversed(lists):
    reverse_list = []
    n = len(lists) - 1
    if n < 0:
        return reverse_list
    else:
        reverse_list.append(lists[n])
        return reverse_list + get_reversed(lists[:n])

print(get_reversed([1,2,3,4]))