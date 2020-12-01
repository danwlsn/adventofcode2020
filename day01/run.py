MAGIC_NUMBER = 2020


def read_file(file_name):
    with open(file_name) as f:
        file_data = f.read().splitlines()

    f.close()
    return file_data


def find_sum_parts(inputs):

    for a in inputs:
        find = MAGIC_NUMBER - int(a)
        for b in inputs:
            find_l2 = find - int(b)

            if str(find_l2) in inputs:
                return [int(a), int(b), find_l2]


def main():
    input_list = read_file('input.txt')
    sum_parts = find_sum_parts(input_list)

    print(sum_parts[0] * sum_parts[1] * sum_parts[2])



if __name__ == "__main__":
    # execute only if run as a script
    main()
