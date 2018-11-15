
def generate_grey_code(fields=4, start=1, end=3):
    '''

    :param fields: length of the record
    :param start: smallest integer
    :param end: largest integer
    :return: array in gray code order
    '''

    data = []
    starting_record=[]

    # CREATE FIRST RECORD
    for i in range(0, fields):
        starting_record.append(start)

    # ADD FIRST RECORD TO ARRAY
    for j in range(start, end+1, 1):
        record = starting_record[:-1]
        record.append(j)
        data.append(record)

    # MOVING FROM SECOND TO LAST FIELD POSITION FORWARD
    for position in range(fields-2, -1, -1):
        # mirror n times with iterating
        temp_data = []
        counter = 0

        # GENERATE n FOLDS IN THE RANGE OF POSSIBLE INTEGER VALUES
        for fold in range(start, end, 1):

            # IS THE CURRENT FOLD IS EVEN DECREMENT THE VALUES
            # AND ADD GENERATED RECORD TO TEMP ARRAY
            if counter % 2 == 0:
                for k in range(len(data)-1, -1, -1):
                    record = data[k].copy()
                    record[position] = fold+1
                    temp_data.append(record)

            # IS THE CURRENT FOLD ODD INCREMENT THE VALUES
            # AND ADD GENERATED RECORD TO TEMP ARRAY
            else:
                for k in range(0, len(data), 1):
                    record = data[k].copy()
                    record[position] = fold+1
                    temp_data.append(record)

            # INCREMENT COUNTER TO KEEP TRACK OF FOLDS
            counter += 1
        # WHEN THE CURRENT FOLD IS COMPLETE ADD THE GENERATED RECORDS TO THE DATA
        data += temp_data


    return data
if __name__=="__main__":
    print(generate_grey_code())