def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 1

    while left <= right:
        mid = (left + right) // 2
        print("------------------")
        print("left:", left)
        print("right:", right)
        print("mid:", mid)

        if arr[mid] == target:
            print("Target found at index ", mid)
            break

        elif arr[mid] < target:
            left = mid + 1
    
        else:
            right = mid - 1

        iterations += 1
    
    print("Number of iterations: ", iterations)

def generate_sorted_array(size):
    """Generate a sorted array of given size with sequential integers."""
    return list(range(size))

if __name__ == "__main__":
    size = int(input("Enter the array size:"))
    arr = generate_sorted_array(size)
    print("The list is: ", arr)
    target = int(input("Enter the number to find:"))
    binary_search(arr, target)

# def binary_search(arr, target):
#     """
#     Perform binary search on a sorted array to find the index of the target value.

#     Parameters:
#     arr (list): A list of sorted elements.
#     target: The element to search for in the list.

#     Returns:
#     int: The index of the target element if found, otherwise -1.
#     """
#     left, right = 0, len(arr) - 1

#     while left <= right:
#         mid = left + (right - left) // 2

#         # Check if target is present at mid
#         if arr[mid] == target:
#             return mid
#         # If target is greater, ignore left half
#         elif arr[mid] < target:
#             left = mid + 1
#         # If target is smaller, ignore right half
#         else:
#             right = mid - 1

#     # Target was not found in the array
#     return -1



# if __name__ == "__main__":
#     import time

#     sizes = [10**3, 10**4, 10**5, 10**6, 10**7]
#     target = -1  # Target not in the array to test worst-case performance

#     for size in sizes:
#         arr = generate_sorted_array(size)
#         start_time = time.time()
#         result = binary_search(arr, target)
#         end_time = time.time()
#         elapsed_time = end_time - start_time
#         print(f"Array Size: {size}, Time Taken: {elapsed_time:.6f} seconds, Result: {result}")