id_list = [line.rstrip() for line in open('input', 'r')]

for box_id in id_list:
    for compare_box_id in id_list:
        differences = 0

        for n in range(len(box_id)):
            if box_id[n] != compare_box_id[n]:
                differences += 1
                different_index = n
                if differences >= 2:
                    break

        if differences == 1:
            shared_chars = box_id[:different_index] + box_id[different_index+1:]
            print("Matching box ids: {} and {} with shared letters of: {}".format(box_id, compare_box_id, shared_chars))
            exit()


