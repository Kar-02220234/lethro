def bubble_sort_2d(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr[i])):
            for k in range(len(arr[i]) - 1 - j):
                row1 = j // len(arr[i])
                col1 = j % len(arr[i])

                row2 = (j + 1) // len(arr[i])
                col2 = (j + 1) % len(arr[i])

                if arr[row1][col1] > arr[row2][col2]:
                    arr[row1][col1], arr[row2][col2] = arr[row2][col2], arr[row1][col1]

def search_element(arr, element):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == element:
                print(f"element found at position: row = {i}, column = {j}")
                return
    print("element not found in the given array.")

arr =[[9, 2, 3],
      [4, 5, 6],
      [7, 8, 1]]
print(arr)
bubble_sort_2d(arr)
print(arr)

search = int(input("enter the element to search:"))
search_element(arr, search)