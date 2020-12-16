# Read in a message
message = input("Give me a message: ")
# Read in a keyword
key = input("Give me a key word: ").upper()
#Encode or decode?
choice = 0
while (choice!= 1 and choice !=2):
    choice = int(input("Type 1 for encode\nType 2 for decode\n"))
# Set up a variable to keep track of the output
output=""
# Set up a variable to keep track of the position on the key
pos=0
# Loop through the letters of the message:
for letter in message:
# If the current letter is not alphabetical:
    if not letter.isalpha():
        # add the current character to the output
        output+=letter
        # skip to the next loop
        continue

    # Take the letter of the key at “position” and find its numerical value
    # Subtract the numerical value of “A” from the key letter. This is your shift
    shift = ord(key[pos])-ord("A")
    # Find the numerical value of the current letter
    value = ord(letter)
    # Add the shift
    if choice==1:
        value+=shift
        if (letter.islower() and value> ord('z')) or (letter.isupper() and value>ord('Z')):
            value-=26
    else:
        value-=shift
        if (letter.islower() and value<ord('a')) or (letter.isupper() and value<ord('A')):
            value+=26
    # If the new shifted letter is past ‘Z’
    # subtract 26 from the letter
    # turn the numerical value back into a letter
    outputLetter = chr(value)
    # Add the letter to the output string
    output+=outputLetter
    # increase the position for the key word
    pos=(pos+1)%len(key)
# Print the output
print(output)
