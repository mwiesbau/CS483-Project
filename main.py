
import random
from generator import generate_grey_code
from algorithms import radix_sort
class FileOfRecords():
    num_fields = 0
    records = []
    initial_score = {}
    start_int = 0
    end_ind = 0

    def __init__(self, num_records, num_fields, start_int, end_int):
        self.start_int = start_int
        self.end_int = end_int
        self.num_fields = num_fields
        self.start_int = start_int
        self.end_int = end_int

        # GENERATE RECORD DATA
        for j in range(0, num_records):
                self.records.append([])
                for k in range(0, num_fields):
                    self.records[j].append(random.randint(start_int, end_int-1))

        # CALCULATE INITIAL SCORES
        self.initial_score = self.get_score()


    def __str__(self):
        result = ""
        for item in self.records:
            result += "{}\n".format(item)
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


    def algorithm_a(self):
        '''
        Uses grayorder(X,Y) from section 3 in the Paper
        :return: number of loop iterations
        '''

        return None

    def algorithm_b(self):
        '''
        Calculates the rank first with left to right horners rule
        Rank will be m+1 st field
        :return:
        '''

        return None


    def algorithm_c(self):
        '''
        Uses the RADIX sorting from section 4 in the paper
        '''
        sorted_records, number_of_iterations = radix_sort(self.records, num_fields=self.num_fields)
        self.records = sorted_records
        return number_of_iterations

if __name__ == "__main__":


    file_of_records = FileOfRecords(num_records=10000, num_fields=20, start_int=2, end_int=10)


    number_of_ops = file_of_records.algorithm_c()
    print("Statistics for Algorithm C")
    print("="*50)
    print("Operations:     {}".format(number_of_ops))
    print("Before Sorting: {}".format(file_of_records.initial_score))
    print("After Sorting:  {}".format(file_of_records.get_score()))
