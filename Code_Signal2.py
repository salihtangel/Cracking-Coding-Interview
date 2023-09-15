def calculate_total_subarray_sums(input_array):
    n = len(input_array)
    total_sum = 0

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            subarray = input_array[i:i + length]
            subarray_sum = sum(subarray)
            total_sum += subarray_sum

    return total_sum

input_array = [9, 8, 7, 6, 5]
total_sum = calculate_total_subarray_sums(input_array)
print("Total sum of consecutive subarrays:", total_sum)
