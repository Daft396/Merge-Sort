import random
arr = []
def generate_random_list():
    size = int(input("Enter the size of the list: "))
    lower_bound=int(input("Enter the lower bound: "))
    upper_bound=int(input("Enter the upper bound: "))
    
    for i in range(size):
        arr.append(random.randint(lower_bound,upper_bound))

    


def validate_input(input_str):
    pass

def print_list():
    return(arr)
