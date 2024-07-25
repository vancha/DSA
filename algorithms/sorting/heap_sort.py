#used for sorting in ascending order
def max_heapify(arr, n, current):
    largest         = current
    left_child      = 2 * current + 1
    right_child     = 2 * current + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != current:
        arr[current], arr[largest] = arr[largest], arr[current]
        max_heapify(arr, n, largest)

#used for sorting in descending order
def min_heapify(arr, n, current):
    smallest = current
    left_child = 2 * current + 1
    right_child = 2 * current + 2

    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child

    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child

    if smallest != current:
        arr[current], arr[smallest] = arr[smallest], arr[current]
        min_heapify(arr, n, smallest)
      
#build either a min heap or max heap from an array
def build_heap(arr, is_max):
    last_non_leaf_node = (len(arr) // 2) - 1
    for index in range(last_non_leaf_node, -1, -1):
      if is_max:
        max_heapify(arr, len(arr), index)
      else:
        min_heapify(arr, len(arr), index)

#sort an array in ascending order or descending order using a heap
def heap_sort(arr,ascending):
    n = len(arr)
    build_heap(arr, ascending)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        if ascending:
          max_heapify(arr, i, 0)
        else:
          min_heapify(arr, i, 0)

    return arr

#how to use this sorting algorithm:
#arr = [2,34,45,56,3,2,1,3,5,67,7]
#print(heap_sort(arr, False))
