def argmax(array, axis=None):
    col = len(array[0])
    result_array = []
    if axis is None: 
        for a in array:
            result_array += a
        return result_array.index(max(result_array))
    elif axis == 0:
        for i in range(col):
            temp = []
            for a in array:
                temp.append(a[i])
            result_array.append(temp.index(max(temp)))
        return result_array
    elif axis == 1:
        for a in array:
            result_array.append(a.index(max(a)))
        return result_array
    else:
        return "error"

import random

a = [[random.randrange(1, 10) for _ in range(3)] for i in range(3)]
print(a)

print(argmax(a))
print(argmax(a, axis=0))
print(argmax(a, axis=1))