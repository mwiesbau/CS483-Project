from generator import generate_grey_code

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


def grayorder(X, Y):

    d=-1
    # DETERMINE THE LEAST INTEGER d where X[d+1] != Y[d+1]
    for i in range(0, len(X)-1):
        if X[i+1] != Y[i+1]:
            d = i


    # CALCULATE TOTAL D
    total_d = 0
    if d <= 0:
        total_d = 0
    else:
        for i in range(0, d+1):
            total_d += X[i]
    print("d: {} total_d: {}".format(d, total_d))

    if total_d % 2 == 0:
        return (X[d+1] < Y[d+1])
    else:
        return (Y[d+1] < X[d+1])

if __name__ == "__main__":
    #quick_sort(array=unsorted, 0, len(unsorted)-1)
    #print(quick_sort(unsorted, 0, 7))

    grey_code = generate_grey_code(3, 1, 2)
    print(grey_code)
    for i in range(0, len(grey_code)-1):
        print("{} < {} = {}".format(i, i+1,grayorder(grey_code[i], grey_code[i+1])))