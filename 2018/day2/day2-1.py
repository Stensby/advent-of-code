from collections import Counter

id_list = [line.rstrip() for line in open('test_input', 'r')]

two_score = 0
three_score = 0

for box_id in id_list:
    counts = Counter(box_id).values()
    if 2 in counts:
        two_score += 1
    if 3 in counts:
        three_score += 1

checksum = two_score * three_score
print("Checksum is: {}".format(checksum))
