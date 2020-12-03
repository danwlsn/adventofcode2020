def read_inputs(file_name):
    with open(file_name) as f:
        file_data = f.read().splitlines()

    f.close()
    return file_data


def get_password(password_input):
    parts = password_input.split(' ')

    return parts

def is_between(number, range):

    return int(range[0]) <= int(number) <= int(range[1])


def is_valid(password_parts):
    ch_range = password_parts[0].split('-')
    char = password_parts[1].strip(':')
    password = password_parts[2]

    ch_count = password.count(char)
    return is_between(ch_count, ch_range)


def check_pos(password, pos, char):
    return password[int(pos) - 1] == char


def is_valid_2(password_parts):
    ch_index = password_parts[0].split('-')
    char = password_parts[1].strip(':')
    password = password_parts[2]

    truth_table = (
        check_pos(password, ch_index[0], char),
        check_pos(password, ch_index[1], char)
    )

    return truth_table.count(True) == 1


def main():
    valid_password_count = 0

    inputs = read_inputs('input.txt')
    for i in inputs:
        password = get_password(i)
        if is_valid_2(password):
            print(f'valid password: {password[2]}')
            valid_password_count += 1


    print(f'Valid passwords: {valid_password_count}')



if __name__ == "__main__":
    main()
