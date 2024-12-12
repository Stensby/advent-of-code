def read_input(file_path):
    with open(file_path, 'r') as file:
        data = [list(line.strip()) for line in file]
    return data

def find_horizontals(x,y,data):
    count = 0
    if not (x-3 < 0) and data[y][x-1] == 'M' and data[y][x-2] == 'A' and data[y][x-3] == 'S':
        count+=1
    if not (x+3 >= len(data[0])) and data[y][x+1] == 'M' and data[y][x+2] == 'A' and data[y][x+3] == 'S':
        count+=1
    return count

def find_verticals(x,y,data):
    count = 0
    if not (y-3 < 0) and data[y-1][x] == 'M' and data[y-2][x] == 'A' and data[y-3][x] == 'S':
        count+=1
    if not (y+3 >= len(data)) and data[y+1][x] == 'M' and data[y+2][x] == 'A' and data[y+3][x] == 'S':
        count+=1
    return count

def find_diagonals(x,y,data):
    count = 0
    # up left
    if not (y-3 < 0) and not (x-3 < 0) and data[y-1][x-1] == 'M' and data[y-2][x-2] == 'A' and data[y-3][x-3] == 'S':
        count+=1
    # up right
    if not (y-3 < 0) and not (x+3 >= len(data[0])) and data[y-1][x+1] == 'M' and data[y-2][x+2] == 'A' and data[y-3][x+3] == 'S':
        count+=1
    # down left
    if not (y+3 >= len(data)) and not (x-3 < 0) and data[y+1][x-1] == 'M' and data[y+2][x-2] == 'A' and data[y+3][x-3] == 'S':
        count+=1
    # down right
    if not (y+3 >= len(data)) and not (x+3 >= len(data[0])) and data[y+1][x+1] == 'M' and data[y+2][x+2] == 'A' and data[y+3][x+3] == 'S':
        count+=1

    return count



def find_all_xmas(input_data):
    xmas_count = 0
    for y in range(len(input_data)):
        for x in range(len(input_data[0])):
            if input_data[y][x] == 'X':
                xmas_count+=find_horizontals(x,y,input_data)
                xmas_count+=find_verticals(x,y,input_data)
                xmas_count+=find_diagonals(x,y,input_data)

    return xmas_count


if __name__ == "__main__":
    input_data = read_input('input.txt')
    result = find_all_xmas(input_data)
    print(result)
