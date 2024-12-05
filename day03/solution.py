import re

file = open("input.txt", "r")
content=file.read()

sum = 0
for a, b in re.findall(r"mul\((\d+),(\d+)\)", content):
    sum += int(a) * int(b)

enabled_sum = 0
enabled = True
for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", content):
    if do or dont:
        enabled = bool(do)
    else:
        x = int(a) * int(b)
        enabled_sum += x * enabled

print("Solution Part 1: " + str(sum))
print("Solution Part 2: " + str(enabled_sum))