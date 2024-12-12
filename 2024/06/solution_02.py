def read_input(file_path):
    with open(file_path, 'r') as file:
        data = [list(line.strip()) for line in file]
    return data

def guard_path(x, y, map, direction):
    entered_spaces = []
    entered_spaces.append((x, y))
    guard_in_area = False
    if direction == 'up':
        for i in range(y, -1, -1):
            if map[i][x] == '#':
                guard_in_area = True
                direction = 'right'
                break
            entered_spaces.append((x, i))

    elif direction == 'right':
        for i in range(x, len(map[y])):
            if map[y][i] == '#':
                guard_in_area = True
                direction = 'down'
                break
            entered_spaces.append((i, y))

    elif direction == 'down':
        for i in range(y, len(map)):
            if map[i][x] == '#':
                guard_in_area = True
                direction = 'left'
                break
            entered_spaces.append((x, i))

    elif direction == 'left':
        for i in range(x, -1, -1):
            if map[y][i] == '#':
                guard_in_area = True
                direction = 'up'
                break
            entered_spaces.append((i, y))

    else:
        raise ValueError("Invalid direction, how did you get here?")
    return entered_spaces, guard_in_area, direction


def infinite_guard_path(x,y,map):
    guard_in_area = True
    direction = 'up'
    entered_spaces = []
    while guard_in_area:
        spaces, guard_in_area, direction = guard_path(x,y,map, direction)
        x = spaces[-1][0]
        y = spaces[-1][1]
        if spaces not in entered_spaces:
            entered_spaces.append(spaces)
        else:
            return True
    return False


if __name__ == "__main__":
    input_data = read_input('input.txt')
    # Find guard location
    for y in range(len(input_data)):
        for x in range(len(input_data[y])):
            if input_data[y][x] == '^':
                guard = (x, y)
                break

    print("Guard found at x: {}, y: {}".format(x, y))

    # Update tiles one at a time, check if completable
    obstructions = []
    for y in range(len(input_data)):
        for x in range(len(input_data[y])):
            if input_data[y][x] == '.':
                input_data[y][x] = '#' 
                if infinite_guard_path(guard[0],guard[1],input_data):
                    obstructions.append((x,y))
                input_data[y][x] = '.'

    print(obstructions)
    print(len(obstructions))
