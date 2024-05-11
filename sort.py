arr = [1, 3, 5, 2, 6, 7, 10, 4]


def sort(arr):
    for m in range(0, len(arr)):
        for n in range(0, len(arr) - 1 - m):
            if arr[n] > arr[n + 1]:
                arr[n], arr[n + 1] = arr[n + 1], arr[n]

    return arr


sort(arr)

print(arr)
