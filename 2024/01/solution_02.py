def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # read in two lists, with first list being the first element per row and second list being the second element per row
        list1 = [int(line.split()[0]) for line in lines]
        list2 = [int(line.split()[1]) for line in lines]
    return list1, list2

def frequency_count_by_element(list):
    frequency = {}
    for i in range(len(list)):
        if list[i] in frequency:
            frequency[list[i]] += 1
        else:
            frequency[list[i]] = 1
    return frequency

def calculate_similarity_score(list1, list2):
    score = 0
    frequency_list = frequency_count_by_element(list2)
    for element in list1:
        score += frequency_list.get(element, 0) * element
            
    return score

if __name__ == "__main__":
    list1, list2 = read_input('input.txt')
    list1.sort()
    list2.sort()
    solution = calculate_similarity_score(list1, list2)
    print("Similarity score between lists is: ", solution)
