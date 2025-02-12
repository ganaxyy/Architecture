
print("=== Linear Search Program ===")

print("Enter the elements of the array separated by spaces:")
user_input = input().split()
array = []

for item in user_input:
    try:
        array.append(int(item))
    except ValueError:
        array.append(item)

print(f"Array created: {array}")

print("Enter the target element to search for:")
target_input = input()
try:
    target = int(target_input)
except ValueError:
    target = target_input

print(f"Target to search: {target}")

indices = []
count = 0

print(f"Searching for '{target}' in the array: {array}")

for index in range(len(array)):
    print(f"Checking index {index}, value: {array[index]}")
    
    if array[index] == target:
        indices.append(index)
        count += 1
        print(f"Match found at index {index}")
        continue
    else:
        continue

if count > 0:
    print(f"\n'{target}' found {count} times at indices: {indices}")
else:
    print(f"\n'{target}' not found in the array.")

print("\n=== Search Completed ===")
