arr = [2, 3, 4, 9, 5, 7, 8, 6, 1]

n = len(arr)

for j in range(n - 1):
    iMin = j
    for i in range(j + 1, n):
        if arr[i] < arr[iMin]:
            iMin = i
    print(f"{arr[iMin]} <> {arr[j]}")
    if iMin != j:
        arr[j], arr[iMin] = arr[iMin], arr[j]

print(arr)
