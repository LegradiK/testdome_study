def count_numbers(sorted_list, less_than):
    low, high = 0, len(sorted_list)
    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] < less_than:
            low = mid + 1   # answer is to the right of mid
        else:
            high = mid      # mid might be the first item >= less_than
    return low
        

    
sorted_list = [1, 3, 5, 7]
print(count_numbers(sorted_list, 4)) # should print 2