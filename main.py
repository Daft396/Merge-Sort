from sort import merge_sort

from utils import generate_random_list,validate_input,print_list


print("="*100)
print("Welcome to the merge sort program!")

generate_random_list()
print("Unsorted List", print_list())
print('\n')
print("Sorted List", merge_sort(print_list()))
next_attempt = input("Do you want to sort another list? y/n?: ")
while next_attempt == "Y" or next_attempt == "y":
    print('\n')
    generate_random_list()
    print("Unsorted List", print_list())
    print('\n')
    print("Sorted List", merge_sort(print_list()))
    next_attempt = input("Do you want to sort another list? y/n?: ")
exit()
print("="*100)
