def linear_search(arr, data):
    for i in range (0, len(arr)):
        if (arr[i] == data):
            return i
    return -1

arr = [12,21,34,38,40]
data = 30
res = linear_search(arr, data)
print(res)