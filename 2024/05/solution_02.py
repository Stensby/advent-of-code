from functools import cmp_to_key

def read_and_split_file(file_path):
    with open(file_path, 'r') as file:
        instructions = []
        print_order = []
        
        for line in file:
            line = line.strip()
            if '|' in line:
                instructions.append(line.split('|'))
            elif ',' in line:
                print_order.append(line.split(','))
        
    return instructions, print_order

def get_sort_order(instructions):
    sort_order = []
    for instruction in instructions:
        if instruction[0] not in sort_order:
            sort_order.append(instruction[0])
        else:
            sort_order.insert(0, instruction[0])
        if instruction[1] not in sort_order:
            sort_order.append(instruction[1])

    return sort_order

def custom_compare(a, b):
    if [str(a), str(b)] in instructions:
        return -1
    elif [str(b), str(a)] in instructions:
        return 1
    elif a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def update_order(instructions, print_line):
    return sorted(print_line, key=cmp_to_key(custom_compare))


def validate_print_order(instructions, print_order):
    incorrect_ordered_prints = []
    sum_middle_elements = 0
    for print_line in print_order:
        correct_order = True
        for instruction in instructions:
            if instruction[0] in print_line and instruction[1] in print_line:
                if not print_line.index(instruction[0]) < print_line.index(instruction[1]):
                    correct_order = False
                    incorrect_ordered_prints.append(print_line)
                    break
        if not correct_order:
            print_line = update_order(instructions, print_line)
            incorrect_ordered_prints.append(print_line)
            middle_element = print_line[len(print_line)//2]
            sum_middle_elements += int(middle_element)

    return incorrect_ordered_prints, sum_middle_elements

if __name__ == "__main__":
    instructions, print_order = read_and_split_file('input.txt')

    correct_ordered_prints, sum_middle_elements = validate_print_order(instructions, print_order)
    
    print("Correct ordered print sum, count:", sum_middle_elements, len(correct_ordered_prints))
