sum_freq = 0
with open('.//input.txt') as txtInputFile:
    for line in txtInputFile:
        sum_freq = sum_freq + int(line)

print(sum_freq)
