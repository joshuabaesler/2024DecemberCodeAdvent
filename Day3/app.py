import re
#Part 1

file = open("Day3/input.txt", "r") 
fullFile = ""
for line in file:
    fullFile+= line
file.close

regMatch = re.findall("[mul]{3}[(][0-9]+[,][0-9]+[)]",fullFile)
totalSum = 0
for entry in regMatch:
    #get the numbers, mult, then add a total sum
    split = entry.replace("mul(","").replace(")","").split(",")
    thisSum = int(split[0]) * int(split[1])
    totalSum += thisSum

print("The Total Multiplication Sum:")
print(totalSum)

#Part 2
regMatch = re.findall("([do]{2}[()]{2}.*[mul]{3}[(][0-9]+[,][0-9]+[)])",fullFile)
totalSum = 0

print(len(regMatch))

for matchList in regMatch:
    # get the numbers, mult, then add a total sum
    secondLevelMatch = re.search("((?!don't()).)*[mul]{3}[(][0-9]+[,][0-9]+[)]", matchList[0])
    print(secondLevelMatch)
    #split = secondLevelMatch.replace("mul(","").replace(")","").split(",")
    #thisSum = int(split[0]) * int(split[1])
    #totalSum += thisSum

print("The Total Multiplication Sum:")
print(totalSum)