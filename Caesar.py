#You have to read in a message as a string
message = input("Enter a message: ")
output=""
#You have to read in a shift as a number (1-25)
shift = int(input("Enter a shift (1-25)"))%26
#You have to loop through every letter
for letter in message:
	#if the character is not a letter:
    if not (letter.isalpha()):
		#go to the next letter
        output+=letter
        continue
    #Check for Upper/Lower case
    if letter.islower():
        lowerCase=True
    else:
        lowerCase=False
	#turn the letter into a number
    value = ord(letter)
	#add the shift to the letter
    value+=shift
	#if the letter is over the edge of the alphabet
    if (lowerCase and value>ord('z')) or (not lowerCase and value>ord('Z')):
		#subtract 26 from the letter
        value-=26
	#turn the number back to a letter
    value=chr(value)
    #print the letter
    output+=value
print(output)
#this is a change
