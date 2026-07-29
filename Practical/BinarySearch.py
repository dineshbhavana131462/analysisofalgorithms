# Binary Search

n = int(input("Enter the number of elements: "))
arr = []

print("Enter the sorted elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at index", mid)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")
