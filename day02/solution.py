def readFile(textfile):
    file = open(textfile, "r")
    reports = []
    while True:
        content=file.readline()
        if not content:
            break
        reports.append(content.split())
    return reports

def isReportSafe(report):
    safe = True
    increasing = True

    for k in range(0, len(report)-1):
        diff = abs(int(report[k]) - int(report[k+1]))
        if (diff < 1 or diff > 3):
            safe = False
            break
        if (k == 0) and (int(report[k]) > int(report[k+1])):
            increasing = False
            continue
        
        if increasing and (int(report[k]) > int(report[k+1])):
            safe = False
            break
        
        if (not increasing) and (int(report[k]) < int(report[k+1])):
            safe = False
            break
    return safe

reports = readFile("input.txt")
safe_count = 0
partially_safe_count = 0
for i in range(len(reports)):
    safe = isReportSafe(reports[i])
    if safe:
        safe_count+=1
        partially_safe_count+=1
    else:
        for l in range(0, len(reports[i])):
            partial_report = reports[i][:l] + reports[i][l+1:]
            safe = isReportSafe(partial_report)
            if safe:
                partially_safe_count+=1
                break

print("Solution Part 1: " + str(safe_count))
print("Solution Part 2: " + str(partially_safe_count))