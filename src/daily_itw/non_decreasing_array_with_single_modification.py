# You are given an array of integers in an arbitrary order.
# Return whether it is possible to make the array non-decreasing by modifying at most 1 element to any value.

# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
# Example: [13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.
# [13, 4, 1] however, should return false, since there is no way to modify just one element to make the array
# non-decreasing.

def solution(arr):
    chances = 1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            if chances > 0:
                chances = chances - 1
            else:
                return False
    return True


if __name__ == '__main__':
    assert solution([13, 4, 7]) is True
    assert solution([13, 4, 1]) is False
    assert solution([1, 2, 3, 4, 5, 6]) is True
    assert solution([1, 2, 3, 4, 6, 5]) is True
    assert solution([2, 1, 3, 4, 6, 5]) is False
