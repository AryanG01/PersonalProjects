def sort_list(list1):
    result = []
    while list1:
        minimum = list1[0]
        for i in list1:
            if i <= minimum:
                minimum = i
        result.append(minimum)
        list1.remove(minimum)
    return result

data_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sort_list(data_list))