def readFile(textfile):
    file = open("input.txt", "r")
    left = []
    right = []
    while True:
        content=file.readline()
        if not content:
            break
        l, r = content.split()
        left.append(l)
        right.append(r)
    return left, right

left, right = readFile("input.txt")
left = sorted(left)
right = sorted(right)

diff = 0
similarity_score = 0

for i in range(len(left)):
    diff += abs(int(left[i])-int(right[i]))
    similarity_score += int(right.count(left[i])) * int(left[i])

print("Solution Part 1: " + str(diff))
print("Solution Part 2: " + str(similarity_score))


