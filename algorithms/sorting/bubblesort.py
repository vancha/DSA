'''
an implementation of bubble sort, to be used as follows

arr = [3,2,3,4,5,3,12,1]
sort = bubble_sort(arr)
'''
def bubble_sort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-(j+1)):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr


'''
the algorithm goes over ever element of the list
    for j in range(len(arr)-1):
        and does it as often as there are lists, giving it a complexity of o(n^2)
        for i in range(len(arr)-(j+1)):
            #if any two elements are out of order, it performs one swap
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

'''
