def insertion_sort(arr):
    n = len(arr)
    new_arr = [arr[0]]

    for i in range(1,n):
        
        j = 0
        while j < i and new_arr[j] < arr[i]:
            j += 1
        
        new_arr.insert(j, arr[i])

    return new_arr

arr = [3,1,4,5,2]
print(insertion_sort(arr))