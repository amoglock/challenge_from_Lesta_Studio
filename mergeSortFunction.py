def merge(left_list, right_list):
    i, j = 0,0
    result = []
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1
    if i < len(left_list):
        result += left_list[i:]
    if j < len(right_list):
        result += right_list[j:]
    return result

def merge_sort(array: list):
    size = len(array)
    if size == 1:
        return array
    mid = size // 2
    left_list = merge_sort(array[:mid])
    right_list = merge_sort(array[mid:])
    return merge(left_list, right_list)