# Part 1
def safetyCheck(line) -> bool:
    lastNum = int(line[0])
    inc = False
    dec = False

    for i in range(1, len(line)):
        nextNum = int(line[i])
        if(lastNum < nextNum and not dec):
            inc = True
        elif(lastNum > nextNum and not inc):
            dec = True
        else:
            return False

        if( abs(lastNum - nextNum) < 1 or abs(lastNum - nextNum) > 3 ):
            return False
            
        lastNum = nextNum
    return True

file = open("Day2/input.txt", "r") 
inputArr = []
safeCount = 0


for line in file:
    dataArr=line.split()
    if(safetyCheck(dataArr)):
        safeCount +=1
    inputArr.append(dataArr)
file.close

print("Total Safe Count:")
print(safeCount)

safeCount = 0

# Part 2
for line in inputArr:
    safe = safetyCheck(line)
    if(not safe):
        for i in range(0, len(line)):
            newLine = line.copy()
            newLine.pop(i)
            safe = safetyCheck(newLine)
            if(safe):
                break
        
    if(safe):
        safeCount +=1

print("Total Dampened Safe Count:")
print(safeCount)

