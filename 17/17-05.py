def mirror(arr):
    mirrored_part = arr
    mirrored_part = arr[::-1]
    arr += mirrored_part


arr = [1]
mirror(arr)
print(*arr)

