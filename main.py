import numpy as np
import random
import copy
from algorithms import radix_sort, gray_order_sort, rank_sort
import json

class FileOfRecords():

    def __init__(self, num_records, num_fields):
        self.radix_vector = []

        # GENERATE RANDOM RADIX VALUES FOR COLUMNS
        for k in range(0, num_fields):
            Ni = random.randint(2, 10)
            self.radix_vector.append(Ni)

        self.num_fields = num_fields

        # GENERATE RECORD DATA
        self.records = []
        for j in range(0, num_records):
                self.records.append([])
                for k in range(0, num_fields):
                    self.records[j].append(random.randint(0, self.radix_vector[k] - 1))

        # CALCULATE INITIAL SCORES
        self.initial_score = self.get_score()

    def __str__(self):
        result = ""

        for record in self.records:
            result += "{}\n".format(record)
        return result


    def get_score(self):
        '''
        Calculates the binary score by counting the fields with differences for each successive record
        :return: dict containing all scores
        '''
        full_score = 0
        binary_counter = 0
        # ITERATE OVER COLUMNS
        for i in range(0, self.num_fields):
            # ITERATE OVER ROWA
            for j in range(1, len(self.records)):
                # COMPARE CURRENT ROW VALUE WITH PREVIOUS ROW VALUE
                if self.records[j][i] != self.records[j-1][i]:
                    binary_counter += 1
                    full_score += abs(self.records[j][i] - self.records[j-1][i])

                # FOR DEBUGING ONLY
                #else:
                #    print("Row: {} Col: {} is the same as predecessor.".format(j, i))
        return {"binary_score": binary_counter, "full_score": full_score}

    def write_to_file(self):
        np.save("output.npy", self.records)

    def algorithm_a(self):
        '''
        Uses grayorder(X,Y) from section 3 in the Paper
        :return: number of loop iterations
        '''
        sorted_records, number_of_iterations = gray_order_sort(self.records)
        self.records = sorted_records
        return number_of_iterations

    def algorithm_b(self):
        '''
        Calculates the rank first with left to right horners rule
        Rank will be m+1 st field
        :return:
        '''

        sorted_records, number_of_iterations = rank_sort(self.records, 11)

        # REMOVE RANK FROM RECORD
        for i in range(0, len(sorted_records)):
            sorted_records[i] = sorted_records[i][:-1]


        self.records = sorted_records
        return number_of_iterations


    def algorithm_c(self):
        '''
        Uses the RADIX sorting from section 4 in the paper
        '''
        sorted_records, number_of_iterations = radix_sort(self.records)
        self.records = sorted_records
        return number_of_iterations

    def print_first_x_records(self, x):
        for i in range(0, x):
            print("\t"+str(self.records[i]))

    def print_last_x_records(self, x):
        for i in range(len(self.records)-x, len(self.records)):
            print("\t"+str(self.records[i]))

def run_algorithm_a(file_of_records):
    number_of_ops = file_of_records.algorithm_a()
    print("Statistics for Algorithm A")
    print("=" * 50)
    print("Operations:     {}".format(number_of_ops))
    print("Before Sorting: {}".format(file_of_records.initial_score))
    print("After Sorting:  {}".format(file_of_records.get_score()))
    print("\n")


def run_algorithm_b(file_of_records):
    number_of_ops = file_of_records.algorithm_b()
    print("Statistics for Algorithm B")
    print("=" * 50)
    print("Operations:     {}".format(number_of_ops))
    print("Before Sorting: {}".format(file_of_records.initial_score))
    print("After Sorting:  {}".format(file_of_records.get_score()))
    print("\n")


def run_algorithm_c(file_of_records):
    number_of_ops = file_of_records.algorithm_c()
    print("Statistics for Algorithm C")
    print("=" * 50)
    print("Operations:     {}".format(number_of_ops))
    print("Before Sorting: {}".format(file_of_records.initial_score))
    print("After Sorting:  {}".format(file_of_records.get_score()))



class Files():
    '''
    The class containing 10 files with 10k records each, each record having 20 fields
    '''
    def __init__(self, num_files=10):
        self.files = []
        for i in range(0, num_files):
            self.files.append(FileOfRecords(num_records=10000, num_fields=20))




def run_algorithm_x(files, param='a', debug=False):
    '''
    :param files:
    :param param: The algorithm parameter (a, b, c)
    :return:
    '''

    stats = {'total_operations': 0,
             'before_score_binary': 0,
             'before_score_full': 0,
             'after_score_binary': 0,
             'after_score_full': 0}

    # ITERATE OVER THE FILES
    for file_of_records in files.files:

        # STORE SCORES BEFORE THE ALGORITHM IS RUN
        before_score = file_of_records.get_score()
        stats['before_score_binary'] += before_score["binary_score"]
        stats['before_score_full'] += before_score["full_score"]

        # DECIDE WHICH ALGORITHM TO RUN
        if param == 'a':
            operations = file_of_records.algorithm_a()
            stats['total_operations'] += operations
        if param == 'b':
            operations = file_of_records.algorithm_b()
            stats['total_operations'] += operations
        if param == 'c':
            operations = file_of_records.algorithm_c()
            stats['total_operations'] += operations

        # STORE SCORES AFTER THE ALGORITHM IS RUN
        after_score = file_of_records.get_score()
        stats['after_score_binary'] += after_score["binary_score"]
        stats['after_score_full'] += after_score["full_score"]

        # DEBUG SECTION SHOWGIN FIRST AND LAST ENTRIES IN SORTED ORDER
        if debug:
            print("-" * 70)
            print("\tFIRST 5 RECORDS IN FILE")
            print("-" * 70)
            file_of_records.print_first_x_records(5)
            print("-" * 70)
            print("\tLAST 5 RECORDS IN FILE")
            print("-" * 70)
            file_of_records.print_last_x_records(5)

    # COMPUTE AVERAGE
    stats['total_operations'] = int(stats['total_operations'] / len(files.files))
    stats['before_score_binary'] = int(stats['before_score_binary'] / len(files.files))
    stats['after_score_binary'] = int(stats['after_score_binary'] / len(files.files))
    stats['before_score_full'] = int(stats['before_score_full'] / len(files.files))
    stats['after_score_full'] = int(stats['after_score_full'] / len(files.files))
    return stats

if __name__ == "__main__":

    # PARAMETTERS TO CONTROL FILES
    number_of_files = 10

    #INITIALIZE THE ALL FILES
    all_files = Files(num_files=number_of_files)

    # LIST OF ALGORITHMS TO RUN
    # a is simple quicksort
    # b is quicksort and computing rank prior
    # c is radix sort
    params = ['a', 'b', 'c']

    for param in params:
        print("\n")
        print("="*70)
        print("Algorithm - {}".format(param.upper()))

        # MAKE COPY THE INSTANCE TO ENSURE THE SAME DATA IS BEING COMPARED
        files = copy.deepcopy(all_files)
        print("\tRunning sample with {} file/s.".format(number_of_files))
        stats = run_algorithm_x(files, param=param)

        print("\n".join("\t{}\t{}".format(k, v) for k, v in stats.items()))
        print("=" * 70)






