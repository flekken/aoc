def read_input():
    all_lines = []
    with open('input.txt') as txtInputFile:
        for line in txtInputFile:
            all_lines.append(int(line))
    return all_lines


lines = read_input()
jumps = 0
index = 0
while len(lines) > index >= 0:
    jumps += 1
    lines[index] += 1
    index = index + lines[index] - 1

print(jumps)
