def sorted_squared_array(arr):
    n = len(arr)
    result = [0] * n
    left, right = 0, n - 1
    for i in range(n - 1, -1, -1):
        if abs(arr[left]) > abs(arr[right]):
            result[i] = arr[left] ** 2
            left += 1
        else:
            result[i] = arr[right] ** 2
            right -= 1
    return result

# Example usage
arr = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
print(sorted_squared_array(arr))
