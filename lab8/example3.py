def get_evens(a_list):
    n = len(a_list) - 1
    counter = 0
    if n < 0:
        return counter
    else:
        if a_list[n] % 2 == 0:
            counter += 1
            return counter + get_evens(a_list[:n])
        else:
            return counter + get_evens(a_list[:n])

a = [0,1,2,3,4,5]
print(get_evens(a))