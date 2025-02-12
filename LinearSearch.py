
print("=== Binary Search Program ===")

def get_input():
    print("Enter a list of numbers separated by spaces:")
    user_input = input().split()
    array = []
    
    for item in user_input:
        try:
            array.append(int(item))
        except ValueError:
            print(f"Skipping invalid input: {item}")
    
    return array

def sort_array(arr):
    print("Sorting array...")
    sorted_array = sorted(arr)
    print(f"Sorted array: {sorted_array}")
    return sorted_array

def get_target():
    print("Enter the target number to search for:")
    target_input = input()
    try:
        target = int(target_input)
    except ValueError:
        print("Invalid input. Defaulting to -1.")
        target = -1
        
    return target

def binary_search(arr, target):
    print("Performing Binary Search...")
    left = 0
    right = len(arr) - 1
    steps = 0
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        mid_val = arr[mid]
        
        print(f"Step {steps}: Checking middle index {mid}, value: {mid_val}")
        
        if mid_val == target:
            print(f"Match found at index {mid} in {steps} steps.")
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    print("Target not found.")
    return -1

def main():
    array = get_input()
    if len(array) == 0:
        print("Empty array. Exiting...")
        return
    
    sorted_array = sort_array(array)
    target = get_target()
    
    result = binary_search(sorted_array, target)
    if result != -1:
        print(f"Target {target} found at index {result} in the sorted array.")
    else:
        print(f"Target {target} not found in the array.")

    print("\n=== Search Completed ===")

main()
