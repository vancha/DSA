'''
Merge sort algorith, should be used as follows

arr = [2,99, 12, 31, 25, 8, 32, 17, 40, 42]
arr_sorted = merge_sort(arr)

'''
def merge(left_list, right_list):
    output = []
    while left_list or right_list:
        if left_list and right_list:
            if left_list[0] < right_list[0]:
                output.append(left_list.pop(0))
            else:
                output.append(right_list.pop(0)) 
        elif left_list:
            output.append(left_list.pop(0))
        else:
            output.append(right_list.pop(0))
    return output

def merge_sort(lst): 
    exploded_list = [[element] for element in lst]
    while len(exploded_list) > 1:
        for _ in range(len(exploded_list) // 2):
            new_list = merge(exploded_list.pop(0), exploded_list.pop(0))
            exploded_list.append(new_list) 
    return exploded_list[0]
