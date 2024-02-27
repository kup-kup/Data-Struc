def merge_sort(list):
    if len(list) <= 1:
        return list

    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)