with open("file.txt","r") as file:
    lines = file.readlines()
currentdict = {}
for line in lines:
    value = line.split("\t")
    #THE MAIN LOGIC IS TO CONVERT INTO KEY VALUE PAIRS
    currentdict[value[0]] = value[1] 

amount = int(input("ENTER THE AMOUNT YOU WNAT TO CONVERT: "))
print("AVALIABLE OPTIONS: \n " )
for item in currentdict.keys():
    print(item)
choice = input("ENTER THE NAME OF CURRENCY FROM AVAILABLE OPTIONS: ")
#THE NEXT MAIN LOGIC IS TO GET VALUE OF DESIRED CHOICE
total = float(amount * float(currentdict[choice]))
print(f"{amount} in INR IS EQUAL TO approximately {total} of {choice}")