import re

def parse_memory(memory):
    sum = 0
    result = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", memory)
    for r in result:
        r = r.replace("mul(", "").replace(")", "")
        first, second = r.split(",")
        sum += int(first) * int(second)
    return sum
    

if __name__ == "__main__":
    with open("input.txt") as f:
        memory = f.read().strip()
    result = parse_memory(memory)
    print(result)
