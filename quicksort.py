

unsorted = [5, 3, 1, 9, 8, 2, 4, 7]


def partition(arr, left, right):
    '''
    Lomuto Partition scheme
    :param arr:
    :param left:
    :param right:
    :return:
    '''

    pivot = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] <= pivot:
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
    return i


def quick_sort(arr, left, right):

    if left < right:
        part = partition(arr, left, right)
        quick_sort(arr, left, part-1)
        quick_sort(arr, part+1, right)

    return arr

'''
if __name__ == "__main__":
    #quick_sort(array=unsorted, 0, len(unsorted)-1)
    print(quick_sort(unsorted, 0, 7))
'''