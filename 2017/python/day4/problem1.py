valid_line_count = 0
with open('.//input.txt') as txtInputFile:
    for line in txtInputFile:
        words = line.split()
        words_set = set(words)
        if len(words) == len(words_set):
            valid_line_count += 1

print(valid_line_count)
