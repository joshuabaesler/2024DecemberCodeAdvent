import re
#Part 1

file = open("Day3/input.txt", "r") 
fullFile = ""
for line in file:
    fullFile+= line
file.close
fullFile = fullFile.replace("\n", "")

#regex match any mul(*,*) strings
regMatch = re.findall("mul\([0-9]+[,][0-9]+\)",fullFile)
totalSum = 0
for entry in regMatch:
    #get the numbers, mult, then add a total sum
    split = entry.replace("mul(","").replace(")","").split(",")
    thisSum = int(split[0]) * int(split[1])
    totalSum += thisSum

print("The Total Multiplication Sum:")
print(totalSum)

#Part 2

#delete all instances where dont comes before do
regMatch = re.findall("don't\(\).*?do\(\)",fullFile)
newFile = fullFile
for match in regMatch:
    newFile = newFile.replace(match, "")
totalSum = 0

#regex match mul(*,*) as normal
regMatch = re.findall("mul[(][0-9]+[,][0-9]+[)]",newFile)
for match in regMatch:
    # get the numbers, mult, then add a total sum
    split = match.replace("mul(","").replace(")","").split(",")
    thisSum = int(split[0]) * int(split[1])
    totalSum += thisSum

print("The Total Multiplication Sum:")
print(totalSum)