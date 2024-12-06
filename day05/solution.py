def readFile(textfile):
    file = open(textfile, "r")
    page_rules = []
    page_updates = []
    rules = True
    while True:
        content=file.readline()
        if not content:
            break
        if len(content.strip())==0:
            rules = False
            continue
        if rules:
            page_rules.append(content.strip().split("|"))
        else:
            page_updates.append(content.strip().split(","))
    return page_rules, page_updates

def isValid(update, rules):
    for pre, post in page_rules:
        if (pre in update) and (post in update) and (update.index(pre) > update.index(post)):
            return False, pre, post
    return True, "", "" 


page_rules, page_updates = readFile("input.txt")
total_correct = 0
total_swapped = 0

corrupted_updates = []
for update in page_updates:
    valid, _, _ = isValid(update, rules)
    if valid:
        total_correct += int(update[len(update)//2])
    else: 
        corrupted_updates.append(update)


for update in corrupted_updates:
    valid = False
    while not valid:
        valid, pre, post = isValid(update, rules)
        if not valid:
            pre_idx = update.index(pre)
            post_idx = update.index(post)
            update[pre_idx] = post
            update[post_idx] = pre
    total_swapped += int(update[len(update)//2])

print("Solution Part 1: " + str(total_correct))
print("Solution Part 2: " + str(total_swapped))