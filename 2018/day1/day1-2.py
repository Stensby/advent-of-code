input_file = open("input", "r")
frequency_list = input_file.readlines()

previous_frequency_list = [0]
frequency = 0
while True:
    for change in frequency_list:
        frequency += int(change)
        if frequency in previous_frequency_list:
            print("First repeated frequency is: {}".format(frequency))
            exit()
        previous_frequency_list.append(frequency)
