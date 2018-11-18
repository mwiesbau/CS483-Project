import numpy as np
import random
from algorithms import radix_sort, gray_order_sort, rank_sort

class FileOfRecords():
    #num_fields = 0
    #records = []
    #initial_score = {}
    #start_int = 0
    #end_ind = 0

    def __init__(self, num_records, num_fields):
        self.num_fields = num_fields
        #random.seed(3)
        # GENERATE RECORD DATA
        self.records = []
        for j in range(0, num_records):
                Ni = random.randint(2,10)
                self.records.append([])
                for k in range(0, num_fields):
                    self.records[j].append(random.randint(1, Ni))

        # CALCULATE INITIAL SCORES
        #self.initial_score = self.get_score()

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

        sorted_records, number_of_iterations = rank_sort(self.records, 10)
        self.records = sorted_records
        return number_of_iterations


    def algorithm_c(self):
        '''
        Uses the RADIX sorting from section 4 in the paper
        '''
        sorted_records, number_of_iterations = radix_sort(self.records, num_fields=self.num_fields)
        self.records = sorted_records
        return number_of_iterations


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



    def __init__(self, num_files=10):
        self.records = []
        for i in range(0, num_files):
            self.records.append(FileOfRecords(num_records=10000, num_fields=20))





if __name__ == "__main__":

    #file_of_records_a = FileOfRecords(num_records=10000, num_fields=20)

    params = ['a', 'b', 'c']    # LIST OF ALGORITHMS TO RUN

    for param in params:
        print("\nRunning Algorithm: {}".format(param))
        counter = 0
        total_counter = 0
        before_binary = 0
        before_full = 0
        after_binary = 0
        after_full = 0
        total_operations = 0
        for i in range(0,10):
            counter += 1

            file_records = Files()
            print("\tRunning {:02d}/10 samples with 10 files.".format(counter))

            for file_of_records in file_records.records:
                total_counter += 1
                before_score = file_of_records.get_score()
                #print("{} Scores: {}".format(counter, before_score))
                before_binary += before_score["binary_score"]
                before_full += before_score["full_score"]
                if param == 'a':
                    operations = file_of_records.algorithm_a()
                    total_operations += operations
                if param == 'b':
                    operations = file_of_records.algorithm_b()
                    total_operations += operations
                if param == 'c':
                    operations = file_of_records.algorithm_c()
                    total_operations += operations
                after_score = file_of_records.get_score()
                after_binary += after_score["binary_score"]
                after_full += after_score["full_score"]

        print("-"*70)
        print("Before Averages total: {} iterations: Binary: {:.1f}, Full: {:.1f}".format(total_counter, before_binary/total_counter, before_full/total_counter))
        print("After Averages total:  {} iterations: Binary: {:.1f}, Full: {:.1f}".format(total_counter, after_binary /total_counter, after_full /total_counter))
        print("Average Operations: {}".format(total_operations/total_counter))
        print("="*70)




