targetNumber = 361527

currentNumber = 1
currentIndex = 1
previousNumber = 1
while currentNumber < targetNumber:
    previousNumber = currentNumber
    currentNumber += currentIndex * 8
    # print("currentNumber: " + str(currentNumber) + ", index: " + str(currentIndex))
    currentIndex += 1

firstNumber = previousNumber + 1
cornerSize = (currentIndex - 1) * 2
middleNumber = (currentIndex - 1)
# search for the number in corner indexes
targetIndex = cornerSize
isDecreasing = True
# print("m: " + str(middleNumber) + ", cs: " + str(cornerSize))
for squareNumber in range(firstNumber, targetNumber + 1):
    if isDecreasing and targetIndex > middleNumber:
        targetIndex = targetIndex - 1
        if targetIndex == middleNumber:
            isDecreasing = False
    else:
        targetIndex = targetIndex + 1
        if targetIndex == cornerSize:
            isDecreasing = True

print("targetNumber: " + str(targetNumber) + ", targetIndex: " + str(targetIndex))
