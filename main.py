
import random
from generator import generate_grey_code

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

        # START WITH THE LAST FIELD AND ITERATE TO THE FIRST FIELD
        for i in range(self.num_fields-1, -1, -1):
            ordered_array = [] # TEMPORARY ARRAY LOCATION
            sorted_dict = {}   # LIST TO STORE SORTED RESULTS
            # ITERATE OVER ALL RECORDS
            for record in self.records:
                number = record[i]
                # IF THERE IS NO DICT KEY WITH THAT NUMBER CREATE A NEW ENTRY
                if not number in sorted_dict.keys():
                    sorted_dict[number] = []
                sorted_dict[number].append(record)



            # CONVERT THE LINKED LIST TO ARRAY
            ordered_keys = sorted(sorted_dict.keys())
            for key in ordered_keys:
                ordered_array += sorted_dict[key]

            # UPDATE RECORDS
            self.records = ordered_array

            # DBUGING ONLY
            # print(sorted_dict)
            #for item in ordered_array:
            #    print(item)


if __name__ == "__main__":


    file_of_records = FileOfRecords(num_records=25, num_fields=4, start_int=2, end_int=10)


    file_of_records.algorithm_c()
    print("Before Sorting: {}".format(file_of_records.initial_score))
    print("After Sorting: {}".format(file_of_records.get_score()))
