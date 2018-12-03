lines = []
target_line = ""
diff_index = 0
with open('.//input.txt') as txtInputFile:
    for line in txtInputFile:
        for prev_line in lines:
            diff = 0
            for index, char in enumerate(line):
                if char != prev_line[index]:
                    diff = diff + 1
                    if diff == 1:
                        diff_index = index
                    if diff == 2:
                        break
            if diff == 1:
                target_line = line
                break
        lines.append(line)

diff_index = diff_index - 1
target_line = target_line[:diff_index] + target_line[(diff_index + 1):]
print(target_line)
