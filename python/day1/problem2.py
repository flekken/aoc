import os


def get_character_count(txt):
    count = 0
    for line in txt:
        line = line.strip(os.linesep)
        count = count + len(line)
    # print("charCount: " + str(count))
    return count


valueSum = 0
with open('input.txt') as txtInputFile:
    charCount = get_character_count(txtInputFile)
    jump = charCount / 2
    # print("jump: " + str(jump))
    for currentIndex in range(0, charCount):
        txtInputFile.seek(currentIndex)
        currentChar = txtInputFile.read(1)
        # print("index: " + str(currentIndex) + ", current char: " + currentChar)

        nextCharacterIndex = int((currentIndex + jump) % charCount)
        txtInputFile.seek(nextCharacterIndex)
        nextChar = txtInputFile.read(1)
        # print("nextIndex: " + str(nextCharacterIndex) + ", next char: " + nextChar)

        if currentChar == nextChar:
            # print("same values")
            valueSum = valueSum + int(currentChar)

print("sum: " + str(valueSum))
