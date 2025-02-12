def linear_search(arr, target):

    indices = []
    count = 0

    print(f"Searching for '{target}' in the array: {arr}")

    for index in range(len(arr)):
        print(f"Checking index {index}, value: {arr[index]}")

        if arr[index] == target:
            print(f"Match found at index {index}")
            indices.append(index)
            count += 1
        else:
            print(f"No match at index {index}")

    if count > 0:
        print(f"\n'{target}' found {count} times at indices: {indices}")
    else:
        print(f"\n'{target}' not found in the array.")
    
    return indices

def input_array():

    print("Enter the elements of the array separated by spaces:")
    user_input = input().split()
    
    array = []
    for item in user_input:
        try:
            array.append(int(item))
        except ValueError:
            array.append(item)
    
    print(f"Array created: {array}")
    return array

def input_target():

    print("Enter the target element to search for:")
    target_input = input()
    
    try:
        target = int(target_input)
    except ValueError:
        target = target_input
    
    print(f"Target to search: {target}")
    return target

if __name__ == "__main__":
    print("=== Linear Search Program ===")

    array = input_array()

    target = input_target()

    result = linear_search(array, target)

    print("\n=== Search Completed ===")
