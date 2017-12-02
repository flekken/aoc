from urllib.request import Request, urlopen


def get_input_from_api(url):
    request = Request(url)
    # insert your session cookie
    request.add_header('cookie',
                       'session=')
    with urlopen(request) as response:
        return response.read()


# get the input from the website
url = "https://adventofcode.com/2017/day/2/input"
inputStr = get_input_from_api(url)

# convert from byte string to unicode
inputStr = inputStr.decode('UTF-8')
print(inputStr)

# split up by lines
lines = inputStr.split('\n')
print(lines)

# split up by columns
for i in range(len(lines)):
    lines[i] = lines[i].split('\t')

# now the data is in lines[row][column]
print(lines)

checksum = 0
for rowIndex in range(len(lines)):
    biggestValue = 0
    smallestValue = 0
    currentRow = lines[rowIndex]
    for columnIndex in range(len(currentRow)):
        if currentRow[columnIndex].isdigit():
            currentValue = int(currentRow[columnIndex])
            if currentValue > biggestValue:
                biggestValue = currentValue
            if columnIndex == 0 or currentValue < smallestValue:
                smallestValue = currentValue
    print("big: " + str(biggestValue) + ", small: " + str(smallestValue))
    checksum = checksum + (biggestValue - smallestValue)
print("checksum: " + str(checksum))
