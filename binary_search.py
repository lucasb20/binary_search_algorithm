import time as t

def binary_search(array,target):
    array.sort()

    low = 0
    high = len(array)-1

    begin = t.time()
    end = 0

    while low <= high:
        mid = (low+high)//2
        if array[mid] == target:
            end = t.time()
            elapsed_time = end - begin
            estim_time = round(elapsed_time,6)
            print(f'Tempo gasto: {estim_time}s. ({round((estim_time)/60)}min)')
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return 'NULL'