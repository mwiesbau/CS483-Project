
#unsorted = [5, 3, 1, 9, 8, 2, 4, 7]
#unsorted = [
#            [1,1,0],
#            [2,2,0],
#            [0,0,1],
#            [1,1,1],
#            [0,2,1],
#]


def partition(arr, left, right, is_less_than):
    '''
    Lomuto Partition scheme
    :param arr:
    :param left:
    :param right:
    :return:
    '''

    pivot = arr[right]
    i = left
    iterations = 0
    for j in range(left, right):

        iterations += 1
        #print("{} < {} {}".format(arr[j], pivot, grayorder(arr[j], pivot)))
        if is_less_than(arr[j], pivot):
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1

    temp = arr[right]
    arr[right] = arr[i]
    arr[i] = temp

    # DEBUG ONLY
    #print(arr)
    #print("Pivot: {} value: {}".format(i, arr[i]))
    return i, iterations


def quick_sort(arr, left, right, is_less_than):
    '''
    Quick  expects the a comparator function
    :param arr:
    :param left:
    :param right:
    :param is_less_than: comparator function taking two elements and returning a boolean
    :return:
    '''

    total_iterations = 0
    if left < right:
        part, ops_count = partition(arr, left, right, is_less_than)
        total_iterations += ops_count
        quick_sort(arr, left, part-1, is_less_than)
        quick_sort(arr, part+1, right, is_less_than)

    return arr, total_iterations



'''
if __name__ == "__main__":

    #print(quick_sort(unsorted, 0, 4))
'''


