input_file = open("input", "r")
frequency_list = input_file.readlines()

frequency = sum(int(n) for n in frequency_list)

print(frequency)
