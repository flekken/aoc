two_counts = 0
three_counts = 0
with open('.//input.txt') as txtInputFile:
    for line in txtInputFile:
        unique_chars = []
        unique_chars.extend(line)
        unique_chars = set(unique_chars)
        has_two = False
        has_three = False
        for char in unique_chars:
            sum_duplicates = 0
            for c in line:
                if char == c:
                    sum_duplicates = sum_duplicates + 1

            if sum_duplicates == 2 and not has_two:
                two_counts = two_counts + 1
                has_two = True
            elif sum_duplicates == 3and not has_three:
                three_counts = three_counts + 1
                has_three = True

print(two_counts * three_counts)
