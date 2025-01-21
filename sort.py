def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    
    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def bubble_sort(arr):
    pass

def insertion_sort(arr):
    pass

def linear_search(arr):
    pass

def binary_search(arr):
    arr.sort()
    pass
