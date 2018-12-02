lines = []
with open('.//input.txt') as txtInputFile:
    for line in txtInputFile:
        lines.append(int(line))

index = 0
sum_freq = 0
prev_frequencies = set()
prev_frequencies.add(0)
while True:
    sum_freq = sum_freq + lines[index]
    if sum_freq in prev_frequencies:
        break
    prev_frequencies.add(sum_freq)
    index = (index + 1) % len(lines)

print(sum_freq)
