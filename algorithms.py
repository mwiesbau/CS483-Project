from generator import generate_grey_code
import random

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
    num_fields = 4
    # GENERATE GREY CODE AND SHUFFLE
    grey_code = generate_grey_code(fields=num_fields, start=1, end=3)
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



def gray_order_sort(records, num_fields):
    number_of_iterations = 0
    return records, number_of_iterations

def test_gray_order_sort():
    num_fields = 3
    # GENERATE GREY CODE AND SHUFFLE
    grey_code = generate_grey_code(fields=num_fields, start=1, end=2)
    randomized_grey_code = grey_code.copy()
    random.seed(11)
    random.shuffle(randomized_grey_code)

    # SORT
    sorted_grey, iterations = gray_order_sort(randomized_grey_code, num_fields=num_fields)

    is_different = False
    for grey, sorted in zip(grey_code, sorted_grey):
        if grey != sorted:
            is_different == True

        # FOR DEBUGGING
        print("{} | {} | {}".format(grey, sorted, grey == sorted))
    return is_different







def run_all_tests():

    #### ALGORITHM C TEST
    print("Testing the implemented Algorithms")
    print("="*40)
    print("Radix Sort is working as expected: {}".format(not test_radix_sort()))


if __name__ == "__main__":
    
    #run_all_tests()
    test_gray_order_sort()

