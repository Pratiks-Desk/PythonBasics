# Open textInput.txt fie with intention of Reading it
inputFile= open("Resources/textInput.txt","r")

# Open maleFile.txt fie with intention of Writting it
maleFile= open("Resources/maleFile.txt","w")

# Open fe,aleFile..txt fie with intention of Writting it
femaleFile= open("Resources/femaleFile.txt","w")

#for loop through each line of inputFile
for line in inputFile:
    line_split=line.split()
    if line_split[2]=="M":
        maleFile.write(line)
    else:
        femaleFile.write(line)

inputFile.close()
maleFile.close()
femaleFile.close()