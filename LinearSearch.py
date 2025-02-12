def linear_search(arr, target):
    """
    Linear Search Algorithm to find the target in the array.
    Returns a list of indices where the target is found.
    """
    indices = []  # List to store indices of occurrences
    count = 0     # Counter for occurrences

    print(f"Searching for '{target}' in the array: {arr}")

    # Loop through the array
    for index in range(len(arr)):
        print(f"Checking index {index}, value: {arr[index]}")

        # Check if the current element matches the target
        if arr[index] == target:
            print(f"Match found at index {index}")
            indices.append(index)
            count += 1
        else:
            print(f"No match at index {index}")

    # Final results
    if count > 0:
        print(f"\n'{target}' found {count} times at indices: {indices}")
    else:
        print(f"\n'{target}' not found in the array.")
    
    return indices

def input_array():
    """
    Accepts user input to create an array.
    Supports both numbers and strings.
    """
    print("Enter the elements of the array separated by spaces:")
    user_input = input().split()
    
    # Try to convert inputs to integers, otherwise keep as strings
    array = []
    for item in user_input:
        try:
            array.append(int(item))
        except ValueError:
            array.append(item)
    
    print(f"Array created: {array}")
    return array

def input_target():
    """
    Accepts user input for the target element.
    Supports both numbers and strings.
    """
    print("Enter the target element to search for:")
    target_input = input()
    
    # Try to convert to integer, otherwise keep as string
    try:
        target = int(target_input)
    except ValueError:
        target = target_input
    
    print(f"Target to search: {target}")
    return target

if __name__ == "__main__":
    print("=== Linear Search Program ===")

    # Step 1: Input array from user
    array = input_array()

    # Step 2: Input target element from user
    target = input_target()

    # Step 3: Perform linear search
    result = linear_search(array, target)

    # Step 4: Final message
    print("\n=== Search Completed ===")
