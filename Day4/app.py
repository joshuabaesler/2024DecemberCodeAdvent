#Part 1

file = open("Day4/input.txt", "r") 
fullFile = []
#append file to a grid
for line in file:
    arr = list(line.replace("\n",""))
    fullFile.append(arr)
file.close

sum = 0
#set bounds
rowLen = len(fullFile)
colLen = len(fullFile[0])
#grid iteration
for i in range(rowLen):
    for j in range(colLen):
        #Horizontal XMAS check
        if(j < colLen-3 and fullFile[i][j] == "X" and fullFile[i][j+1] == "M" and fullFile[i][j+2] == "A" and fullFile[i][j+3] == "S"):
            sum +=1
        #Horizontal SAMX check
        if(j < colLen-3 and fullFile[i][j] == "S" and fullFile[i][j+1] == "A" and fullFile[i][j+2] == "M" and fullFile[i][j+3] == "X"):
            sum +=1
        #Vertical XMAS check
        if(i < rowLen-3 and fullFile[i][j] == "X" and fullFile[i+1][j] == "M" and fullFile[i+2][j] == "A" and fullFile[i+3][j] == "S"):
            sum +=1
        #Vertical SAMX check
        if(i < rowLen-3 and fullFile[i][j] == "S" and fullFile[i+1][j] == "A" and fullFile[i+2][j] == "M" and fullFile[i+3][j] == "X"):
            sum +=1
        #Diagonal right XMAS check
        if(i < rowLen-3 and j < rowLen-3 and fullFile[i][j] == "X" and fullFile[i+1][j+1] == "M" and fullFile[i+2][j+2] == "A" and fullFile[i+3][j+3] == "S"):
            sum +=1
        #Diagonal right SAMX check
        if(i < rowLen-3 and j < rowLen-3 and fullFile[i][j] == "S" and fullFile[i+1][j+1] == "A" and fullFile[i+2][j+2] == "M" and fullFile[i+3][j+3] == "X"):
            sum +=1
        #Diagonal left XMAS check
        if(i < rowLen-3 and j > 2 and fullFile[i][j] == "X" and fullFile[i+1][j-1] == "M" and fullFile[i+2][j-2] == "A" and fullFile[i+3][j-3] == "S"):
            sum +=1
        #Diagonal left SAMX check
        if(i < rowLen-3 and j > 2 and fullFile[i][j] == "S" and fullFile[i+1][j-1] == "A" and fullFile[i+2][j-2] == "M" and fullFile[i+3][j-3] == "X"):
            sum +=1
print("XMAS Appearances")
print(sum)

#Part 2
sum = 0
#grid iteration
for i in range(rowLen):
    for j in range(colLen):
        xCheck = 0
        #Diagonal right MAS check
        if(i > 0 and j > 0 and i < rowLen-1 and j < colLen-1 and fullFile[i][j] == "A" and fullFile[i-1][j-1] == "M" and fullFile[i+1][j+1] == "S"):
            xCheck +=1
        #Diagonal right SAM check
        if(i > 0 and j > 0 and i < rowLen-1 and j < colLen-1 and fullFile[i][j] == "A" and fullFile[i-1][j-1] == "S" and fullFile[i+1][j+1] == "M"):
            xCheck +=1
        #Diagonal left MAS check
        if(i > 0 and j > 0 and i < rowLen-1 and j < colLen-1 and fullFile[i][j] == "A" and fullFile[i-1][j+1] == "M" and fullFile[i+1][j-1] == "S"):
            xCheck +=1
        #Diagonal left SAM check
        if(i > 0 and j > 0 and i < rowLen-1 and j < colLen-1 and fullFile[i][j] == "A" and fullFile[i-1][j+1] == "S" and fullFile[i+1][j-1] == "M"):
            xCheck +=1
        #Check if a full X is made
        if(xCheck == 2):
            sum+=1

print("X-MAS Appearances")
print(sum)