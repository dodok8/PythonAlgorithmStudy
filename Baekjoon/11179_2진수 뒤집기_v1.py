inputList = bin(int(input()))
outputList = inputList[0:2] + ''.join(reversed(inputList[2:]))
print(int(outputList,2))
