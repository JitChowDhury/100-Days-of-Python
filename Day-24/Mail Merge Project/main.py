#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Day-24/Mail Merge Project/Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("Day-24/Mail Merge Project/Input/Letters/starting_letter.txt") as file:
    content=file.readlines()

letterNum=1

for name in names:
    name = name.strip()
    with open(f"Day-24/Mail Merge Project/Output/ReadyToSend/Letter{letterNum}",mode="w") as file:
        letterNum=letterNum+1
        fl=content[0].strip()
        firstLine=fl.replace("[name]" , name)
        file.write(firstLine+"\n")
        for line in range(1,len(content)):
            file.write(content[line])
        

