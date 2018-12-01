import random

class QuickSort():

    def __init__(self, comparator_function):
        self.total_iterations = 0

        # INTIALIZING COMPARATOR FOR QUICK SORT
        if comparator_function == 'a':
            self.comparator_function = self.__grayorder

        if comparator_function == 'b':
            self.comparator_function = self.__grayorder_rank

    def __grayorder_rank(self, X, Y):

        if X[-1] < Y[-1]:  # COMPARE RANK VALUES
            return True
        else:
            return False

    def __grayorder(self, X, Y):
        '''
        is_less_than method used by quicksort
        Compares two Gray Order Sequences and returns True if X < Y
        :param X: array
        :param Y: array
        :return: boolean
        '''


        d = -1  # INDEX OF FIRST MISSMATCH -1
        total_d = 0

        # DETERMINE THE LEAST INTEGER d where X[d+1] != Y[d+1]
        for i in range(-1, len(X) - 1):
            self.total_iterations += 1
            if X[i + 1] != Y[i + 1]:
                d = i
                break

        # CALCULATE TOTAL D
        for i in range(0, d + 1):
            self.total_iterations += 1
            total_d += X[i]

        # print("d={} total_d={}".format(d, total_d))
        if total_d % 2 == 0:
            return (X[d + 1] < Y[d + 1])
        else:
            return (Y[d + 1] < X[d + 1])

    def partition(self, arr, left, right, is_less_than):
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
            self.total_iterations +=1

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
        return i


    def quick_sort(self, arr, left, right, *comparator_function):
        '''
        Quick  expects the a comparator function
        :param arr:
        :param left:
        :param right:
        :param is_less_than: comparator function taking two elements and returning a boolean
        :return:
        '''

        if left < right:
            self.total_iterations += 1
            part = self.partition(arr, left, right, self.comparator_function)
            self.quick_sort(arr, left, part-1, self.comparator_function)
            self.quick_sort(arr, part+1, right, self.comparator_function)
        return arr



if __name__ == "__main__":

    def is_less_than(item1, item2):
        if item1 < item2:
            return True
        return False

    # TESTING QUICKSORT
    max_range = 7
    total_iterations = 1

    numbers = list(range(0, max_range))
    comparisons = 0

    for i in range(0,total_iterations):
        qs = QuickSort()
        random.shuffle(numbers)
        arr = qs.quick_sort(numbers, 0, max_range-1, is_less_than)
        comparisons += qs.total_iterations
        #print(arr)
        #print(qs.total_iterations)
    print("Total Comparisions: {}".format(comparisons))
    print("Average Effort for n=: {}".format(int(comparisons/total_iterations)))
