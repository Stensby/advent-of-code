import re

def parse_memory(memory):
    sum = 0
    enabled = True
    result = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", memory)
    print(result)
    for r in result:
        if r == "do()":
            enabled = True
            continue
        if r == "don't()":
            enabled = False
            continue
        r = r.replace("mul(", "").replace(")", "")
        first, second = r.split(",")
        if enabled:
            sum += int(first) * int(second)
    return sum
    

if __name__ == "__main__":
    with open("input.txt") as f:
        memory = f.read().strip()
    result = parse_memory(memory)
    print(result)
