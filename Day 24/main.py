#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Letters/starting_letter.txt") as letter:
    new_letter = letter.read()
with open("./Input/Names/invited_names.txt") as names:
    for line in names:
        name = line.strip()
        new_letter_cp = new_letter.replace("[name]",name)
        letter_name = "letter_for_" + name + ".txt"
        with open(f"./Output/ReadyToSend/{letter_name}",mode='w') as letter_file:
                letter_file.write(new_letter_cp)