'''
The array data structure. This file will hold a couple things related to working with arrays:
- searching through an aray
- reversing an array
- rotating an array
- array search,insert and delete in unsorted array
- array search, insert and delete in sorted array
- array sorting
- generation of all subarrays
After which the goal is to use that in solving a couple of leetcode questions

#Rotating an array left

## Rotate left using a temporary array

This approach rotates an array d positions to the left, using the following steps:
    
    - Store index d to the last index in a temporary array
    - append the first index up to d of the original array to the temp array

#Time: O(N)
#Space: O(N)'''
def rotate_array_left(arr, d):
    temp_array = arr[d:len(arr)-1]
    temp_array += arr[0:d]
    return temp_array

'''
## Rotate left one by one

This approach rotates an array left 1 position, using the following steps:
    - store the first element in a temp variable
    - shift all indexes to the left except for the last index
    - set the last index equal to the temp variable

#Time: O(N*d)
#Space: O(1)
'''
def rotate_by_one(arr):
    first = arr[0]
    for (idx,y) in enumerate(arr):
        if idx < len(arr)-1:
            arr[idx] = arr[idx+1]
    arr[len(arr)-1] = first
    return arr
