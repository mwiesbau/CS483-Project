from generator import generate_grey_code
import random
from quicksort import quick_sort

def radix_sort(records, num_fields):
    number_of_iterations = 0
    # START WITH THE LAST FIELD AND ITERATE TO THE FIRST FIELD
    for i in range(num_fields - 1, -1, -1):
        ordered_array = []  # TEMPORARY ARRAY LOCATION
        sorted_dict = {}  # LIST TO STORE SORTED RESULTS

        # ITERATE OVER ALL RECORDS
        for record in records:
            number_of_iterations += 1
            number = record[i]
            # IF THERE IS NO DICT KEY WITH THAT NUMBER CREATE A NEW ENTRY
            if not number in sorted_dict.keys():
                sorted_dict[number] = []

            sorted_dict[number].append(record)

        # CONVERT THE LINKED LIST TO ARRAY
        ordered_keys = sorted(sorted_dict.keys())
        even_odd_counter = 0
        for key in ordered_keys:
            # CHECK IF LIST IS EVEN OR ODD TO ORDER IN GRAY ORDER AND NOT LEXICOGRAPHIC
            if even_odd_counter % 2 == 0:
                ordered_array += sorted_dict[key]
            else:
                ordered_array += reversed(sorted_dict[key])
            even_odd_counter += 1

        # UPDATE RECORDS
        records = ordered_array

        # DBUGING ONLY
        # print(sorted_dict)
        # for item in ordered_array:
        #    print(item)
    return records, number_of_iterations


def test_radix_sort():
    num_fields = 3
    # GENERATE GREY CODE AND SHUFFLE
    grey_code = generate_grey_code(fields=num_fields, start=0, end=2)
    randomized_grey_code = grey_code.copy()
    random.shuffle(randomized_grey_code)

    # SORT
    sorted_grey, iterations = radix_sort(randomized_grey_code, num_fields=num_fields)

    is_different = False
    for grey, sorted in zip(grey_code, sorted_grey):
        if grey != sorted:
            is_different == True

        # FOR DEBUGGING
        #print("{} | {} | {}".format(grey, sorted, grey == sorted))
    return is_different


def grayorder(X, Y):
    '''
    Compares two Gray Order Sequences and returns True if X < Y
    :param X: array
    :param Y: array
    :return: boolean
    '''

    d=-1
    # DETERMINE THE LEAST INTEGER d where X[d+1] != Y[d+1]
    for i in range(-1, len(X)-1):
        if X[i+1] != Y[i+1]:
            d = i
            break

    # CALCULATE TOTAL D
    total_d = 0

    for i in range(0, d+1):
        total_d += X[i]

    #print("d={} total_d={}".format(d, total_d))
    if total_d % 2 == 0:
        return (X[d+1] < Y[d+1])

    else:
        return (Y[d+1] < X[d+1])


def test_grayorder():
    grey_code = generate_grey_code(3, 0, 2)

    is_different = False
    for i in range(0, len(grey_code) - 1):
        if not grayorder(grey_code[i], grey_code[i + 1]):
            is_different = True
    return is_different



def gray_order_sort(records):

    records, number_of_iterations = quick_sort(records, 0, len(records) - 1, grayorder)
    return records, number_of_iterations


def test_gray_order_sort():
    num_fields = 3
    # GENERATE GREY CODE AND SHUFFLE
    grey_code = generate_grey_code(fields=num_fields, start=0, end=2)
    randomized_grey_code = grey_code.copy()
    random.shuffle(randomized_grey_code)

    sorted, iterations = quick_sort(randomized_grey_code, 0, len(randomized_grey_code)-1, grayorder)
    is_different = False

    for grey, sort in zip(grey_code, sorted):

        if grey == sort:
            is_same = True
        else:
            is_different = True
            is_same = False
        #print("{} | {} | {}".format(grey, sort, is_same))
    return is_different


def rank_sort(records, num_fields, N):

    for record in records:
        # ALGORITHM FROM DANA RICHARDS PAPER
        i = record[0]

        for j in range(1, num_fields):
            if i % 2 == 0:
                i_2 = record[j]
            else:
                i_2 = N-1-record[j]

            i = i*N+i_2

        record.append(i)  # APPEND THE RANK TO THE RECORD
    return records

def test_rank_sort():
    num_fields = 3
    # GENERATE GREY CODE AND SHUFFLE
    grey_code = generate_grey_code(fields=num_fields, start=1, end=2)
    randomized_grey_code = grey_code.copy()
    random.shuffle(randomized_grey_code)
    print(rank_sort(grey_code, num_fields, 2))





def run_all_tests():

    #### ALGORITHM C TEST
    print("Testing the implemented Algorithms")
    print("="*40)
    print("Testing Radix Sort")
    print("Radix Sort is working as expected: {}".format(not test_radix_sort()))
    print("-" * 40)

    print("Testing Gray Order")
    print("Gray Order is working as expected: {}".format(not test_grayorder()))
    print("-" * 40)

    print("Testing Gray Order Sort")
    print("Gray Order is working as expected: {}".format(not test_gray_order_sort()))
    print("-" * 40)

if __name__ == "__main__":
    
    run_all_tests()
    #test_gray_order_sort()
    #test_rank_sort()

