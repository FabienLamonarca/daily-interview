def get_range(arr, target):
    bounds = []

    for i in range(0, len(arr)):
        digit = arr[i]
        if digit == target:
            if not bounds:
                bounds.append(i)
                bounds.append(i)
            else:
                if i > bounds[1]:
                    bounds[1] = i

    return bounds if len(bounds) > 0 else [-1, -1]


if __name__ == '__main__':
    assert get_range([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 2) == [1, 4]
