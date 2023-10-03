arr = [2, 3, 4, 1, 5, 7, 8, 6, 9]

for i in range(1, len(arr) - 1):
    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j = j - 1

print(arr)
