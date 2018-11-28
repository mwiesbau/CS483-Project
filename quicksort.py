

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
        _, iter1 = quick_sort(arr, left, part-1, is_less_than)
        _, iter2 = quick_sort(arr, part+1, right, is_less_than)
        total_iterations += ops_count
        total_iterations += iter1
        total_iterations += iter2

    return arr, total_iterations



if __name__ == "__main__":

    items = [3,1,5,9,2,4,7,6,8]

    def is_less_than(item1, item2):
        if item1 < item2:
            return True
        return False

    arr, iterations = quick_sort(items, 0,8, is_less_than)
    print(arr)
    print(iterations)