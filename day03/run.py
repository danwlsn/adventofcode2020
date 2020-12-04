def read_input(file_name):
    with open(file_name) as f:
        file_data = f.read().splitlines()

    f.close()
    return file_data


MAP = read_input('input.txt')
MAP_WIDTH = len(MAP[0])
MAP_HEIGHT = len(MAP)
ROUND_1 = (1, 1)
ROUND_2 = (3, 1)
ROUND_3 = (5, 1)
ROUND_4 = (7, 1)
ROUND_5 = (1, 2)


def get_new_position(current, move=ROUND_1):
    
    x = current[0] + move[0]
    y = current[1] + move[1]
    if x > MAP_WIDTH - 1:
        x = x - MAP_WIDTH

    return x, y


def is_tree(position):
    print(position)
    y = MAP[position[1]]

    return y[position[0]] == '#'


def count_trees_for_path(path):
    tree_count = 0
    position = (0,0)

    for line in MAP:
        if is_tree(position):
            tree_count += 1
        position = get_new_position(position, path)
        if position[1] > MAP_HEIGHT:
            break

    return tree_count


def main():


    print(
        count_trees_for_path(ROUND_1) *
        count_trees_for_path(ROUND_2) *
        count_trees_for_path(ROUND_3) *
        count_trees_for_path(ROUND_4) *
        count_trees_for_path(ROUND_5)
    )

if __name__ == "__main__":
    main()
