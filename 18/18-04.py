def partial_sums(*rest):
    result = [0]
    for elem in rest:
        sum_in_list = result[-1]
        result.append(sum_in_list + elem)
    return result


print(partial_sums(1, 0.5, 0.25, 0.125))