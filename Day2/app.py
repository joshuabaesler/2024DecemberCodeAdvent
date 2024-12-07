# Part 1
file = open("Day2/input.txt", "r") 
inputArr = []
safeCount = 0

for line in file:
    dataArr=line.split()
    lastNum = int(dataArr[0])
    i=1
    incCt = 0
    decCt = 0
    safe = True
    print(dataArr)
    while i < len(dataArr):
        nextNum = int(dataArr[i])
        if(lastNum < nextNum):
            incCt +=1
        elif(lastNum > nextNum):
            decCt +=1

        print(lastNum)
        print(nextNum)
        if( abs(lastNum - nextNum) < 1 or abs(lastNum - nextNum) > 3 ):
            safe = False
            print("here")
            break
        lastNum = nextNum
        i+=1

    print(incCt)
    print(decCt)
    if((incCt == len(dataArr)-1 or decCt == len(dataArr)-1) and safe == True):
        safeCount +=1
    inputArr.append(dataArr)
file.close

print("Total Safe Count:")
print(safeCount)

# Part 2