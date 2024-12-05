# Part 1
file = open("Day1/input.txt", "r") 
col1Arr = []
col2Arr = []
for line in file:
    arr = line.split()
    col1Arr.append(int(arr[0]))
    col2Arr.append(int(arr[1]))
col1Arr.sort()
col2Arr.sort()
file.close

sum = 0
i = 0

while i < len(col1Arr):
    sum += abs((col2Arr[i] - col1Arr[i]))
    i+=1

print("Total Distance is:")
print(sum)



# Part 2

i = 0
similarScore = 0
while i < len(col1Arr):
    j = 0
    similarCount = 0
    while j < len(col2Arr):
        if(col1Arr[i] == col2Arr[j]):
            similarCount +=1
        j+=1

    similarScore += (col1Arr[i] * similarCount)
    i+=1
    
print("Similarity Score is:")
print(similarScore)