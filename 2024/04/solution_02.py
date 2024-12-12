def read_input(file_path):
    with open(file_path, 'r') as file:
        data = [list(line.strip()) for line in file]
    return data

def check_diagonals(x,y,data):
    if (y-1 < 0) or (y+1 >= len(data)) or (x-1 < 0) or (x+1 >= len(data[0])):
        return False

    # if char up left is M and char down right is S or if char up left is S and char down right is M
    if (data[y-1][x-1] == 'M' and data[y+1][x+1] == 'S') or (data[y-1][x-1] == 'S' and data[y+1][x+1] == 'M'):
        # if char up right is M and char down left is S or if char up right is S and char down left is M
        if (data[y-1][x+1] == 'M' and data[y+1][x-1] == 'S') or (data[y-1][x+1] == 'S' and data[y+1][x-1] == 'M'):
            return True

def find_all_xmas(input_data):
    xmas_count = 0
    for y in range(len(input_data)):
        for x in range(len(input_data[0])):
            if input_data[y][x] == 'A':
                if check_diagonals(x,y,input_data):
                    xmas_count+=1

    return xmas_count

if __name__ == "__main__":
    input_data = read_input('input.txt')
    result = find_all_xmas(input_data)
    print(result)
