#Part 1

file = open("Day5/inputFirstHalf.txt", "r") 
firstHalf = []
#append first file to an array split on the | char
for line in file:
    firstHalf.append([page.strip() for page in line.split("|")])
file.close

file = open("Day5/inputSecondHalf.txt", "r") 
secondHalf = []
#append second file to an array
for line in file:
    secondHalf.append(line.replace("\n",""))
file.close

totalMiddles = 0
#loop through second file lines
for line in secondHalf:
    split = line.split(",")
    valid = True
    #then loop the first file pattern lines
    for pattern in firstHalf:
        first = pattern[0]
        second = pattern[1]
        #check if both parts of the pattern are in this line
        if split.__contains__(first) and split.__contains__(second):
            #check if the first part of the pattern comes before the second
            if split.index(first) > split.index(second):
                valid = False
                break
    #get middle element if the string is valid
    if valid:
        totalMiddles += int(split[int((len(split)-1)/2)])
    
print("Total Middle Sum:")
print(totalMiddles)

#Part 2

totalMiddles = 0
#loop through second file lines
for line in secondHalf:
    split = line.split(",")
    valid = True
    totalCorrect = 0
    #while there is a fix occurring, loop until no more fixes need to be made 
    cont = True
    while(cont):
        cont = False
        #then loop the first file pattern lines
        for pattern in firstHalf:
            first = pattern[0]
            second = pattern[1]
            #check if both parts of the pattern are in this line
            if split.__contains__(first) and split.__contains__(second):
                #check if the first part of the pattern comes before the second
                indexFirst = split.index(first)
                indexSecond = split.index(second)
                #if there's pattern mismatch, switch the places to match the pattern
                if indexFirst > indexSecond:
                    valid = False
                    split.__setitem__(indexFirst, second)
                    split.__setitem__(indexSecond, first)
                    cont = True
                
    #get middle element if the string was invalid and fixed 
    if not valid:
        totalMiddles += int(split[int((len(split)-1)/2)])
    
print("Total Fixed Middle Sums:")
print(totalMiddles)