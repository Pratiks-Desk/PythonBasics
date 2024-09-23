inputFile=open("Resources/textInput.txt","r")
print(inputFile.read())
inputFile.close()
print()


inputFile=open("Resources/textInput.txt","r")
for line in inputFile:
    line_spilt=line.split()
    if line_spilt[2]=="M":#[2]-> indexing for Gender column in inputFile. where searching for letter "M".
        print(line)
inputFile.close()