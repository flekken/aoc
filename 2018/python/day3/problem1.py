fabric = [[0 for x in range(1000)] for y in range(1000)]
tuple_list = []
with open('.//input.txt') as txtInputFile:
    for line in txtInputFile:
        parts = line.split(' ')
        origin = parts[2].split(',')
        origin[1] = origin[1][:(len(origin[1]) - 1)]
        size = parts[3].split('x')
        size[1] = size[1].replace('\n', '')
        current_item = (parts[0], int(origin[0]), int(origin[1]), int(size[0]), int(size[1]))
        tuple_list.append(current_item)

goal_id = ""
is_overlap = False
for current_line in tuple_list:
    for compare_line in tuple_list:
        if current_line[0] == compare_line[0]:
            continue
        if not (current_line[1] > compare_line[1] + compare_line[3] or
                current_line[1] + current_line[3] < compare_line[1] or
                current_line[2] > compare_line[2] + compare_line[4] or
                current_line[2] + current_line[4] < compare_line[2]):
            is_overlap = True
            print(current_line)
            print(compare_line)
            break
    if not is_overlap:
        goal_id = current_line[0]
        break
    else:
        is_overlap = False

print(goal_id)
