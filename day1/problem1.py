# opens file with name of "test.txt"
sumOfSameElements = 0
with open('.//day1//input.txt') as txtInputFile:
    firstChr = txtInputFile.read(1)
    lastChr = firstChr
    print(firstChr)
    for line in txtInputFile:
        for ch in line:
            print("char:" + ch + " lastChar:"+lastChr)
            if lastChr == ch:
                sumOfSameElements = sumOfSameElements + int(lastChr)
                print("value increased with: "+ lastChr)
            if ch != "":
                lastChr = ch
    if firstChr == lastChr:
        sumOfSameElements = sumOfSameElements + int(lastChr)
        print("value increased with: "+ lastChr)

print(sumOfSameElements)
