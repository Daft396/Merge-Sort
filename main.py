from sort import merge_sort

from utils import generate_random_list,validate_input,print_list


print("="*100)
print("Welcome to the merge sort program!")

generate_random_list(size,lower_bound,upper_bound)
print("Unsorted List", arr)
print("Sorted List",)
next_attempt = input("Do you want to sort another list? y/n?: ")
if next_attempt == "Y" or next_attempt == "y":
    generate_random_list(size,lower_bound,upper_bound)
else:
    exit()
print("="*100)
