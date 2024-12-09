def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # read in two lists, with first list being the first element per row and second list being the second element per row
        list1 = [int(line.split()[0]) for line in lines]
        list2 = [int(line.split()[1]) for line in lines]
    return list1, list2

def difference_per_element(list1, list2):
    output_list = []
    for i in range(len(list1)):
        output_list.append(abs(list1[i] - list2[i]))
    return output_list


if __name__ == "__main__":
    list1, list2 = read_input('input.txt')
    list1.sort()
    list2.sort()
    distance_list = difference_per_element(list1, list2)
    solution = sum(distance_list)
    print("Total distance between lists is: ", solution)
