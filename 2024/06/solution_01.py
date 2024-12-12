def read_input(file_path):
    with open(file_path, 'r') as file:
        data = [list(line.strip()) for line in file]
    return data

def guard_path(x, y, map, direction):
    entered_spots = []
    entered_spots.append((x, y))
    guard_in_area = False
    if direction == 'up':
        for i in range(y, -1, -1):
            if map[i][x] == '#':
                guard_in_area = True
                direction = 'right'
                break
            entered_spots.append((x, i))

    elif direction == 'right':
        for i in range(x, len(map[y])):
            if map[y][i] == '#':
                guard_in_area = True
                direction = 'down'
                break
            entered_spots.append((i, y))

    elif direction == 'down':
        for i in range(y, len(map)):
            if map[i][x] == '#':
                guard_in_area = True
                direction = 'left'
                break
            entered_spots.append((x, i))

    elif direction == 'left':
        for i in range(x, -1, -1):
            if map[y][i] == '#':
                guard_in_area = True
                direction = 'up'
                break
            entered_spots.append((i, y))

    else:
        raise ValueError("Invalid direction, how did you get here?")
    return entered_spots, guard_in_area, direction

def find_guard_path(x,y,map):
    guard_in_area = True
    direction = 'up'
    entered_spots = set()
    while guard_in_area:
        spaces, guard_in_area, direction = guard_path(x,y,map, direction)
        x = spaces[-1][0]
        y = spaces[-1][1]
        if spaces:
            entered_spots.update(spaces)
    return entered_spots


if __name__ == "__main__":
    input_data = read_input('input.txt')
    for y in range(len(input_data)):
        for x in range(len(input_data[y])):
            if input_data[y][x] == '^':
                break
        if input_data[y][x] == '^':
            break
    print("Guard found at x: {}, y: {}".format(x, y))
    result = find_guard_path(x,y, input_data)
    print(len(result))
