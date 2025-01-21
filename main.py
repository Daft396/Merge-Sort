from sort import *

from utils import generate_random_list,validate_input,print_list

def menu():
    print('\n')
    print("Menu:")
    print("1)create list")
    print("2)sort list")
    print("3)search list")
    print("4)exit")
    choice = int(input("What would you like to do: "))
    
        
    if choice == 1:
        generate_random_list()
        choice = input("would you like to print your list?: ")
        if choice == "Y" or choice == "y":
            print("Unsorted list: ",print_list())
            menu()
        elif choice == "N" or choice == "n":
            menu()

    if choice == 2:
        print("1)insertion sort")
        print("2)bubble sort")
        print("3)merge sort")
        choice = int(input("What sort would you like?: "))
        if choice == 1:
            print('\n')
            print("Sorted list: ",insertion_sort(print_list()))
            menu()
            

        if choice == 2:
            print('\n')
            print("Sorted list: ",bubble_sort(print_list()))
            menu()

        if choice == 3:
            print('\n')
            print("Sorted list: ", merge_sort(print_list()))
            menu()
        

    if choice == 3:
        print("1)linear search")
        print("2)binary search")
        choice = int(input("What kind of search algorithm would you like?: "))
        if choice == 1:
            print('\n')
            print("Sorted list: ",linear_search(print_list()))
            menu()

        if choice == 2:
            print('\n')
            print("Sorted list: ",binary_search(print_list()))
            menu()
            
    if choice == 4:
        print("Thank you for using our program!")
        exit()
                     
print("="*100)
print("Welcome to the merge sort program!")
menu()
print("="*100)
