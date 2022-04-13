vowels = 'aeiou'

while True:
    word = input("Type the word you wish to transform into pig latin: ")
    if word.lower()[0] in vowels:
        # print("should end with 'way'\n")
        piglatin=(word + str("way"))
    else:
        #print( "constanant to the end plus 'ay'\n")
        piglatin= (word[1:] + word[0] + str("ay"))
    print()
    print(piglatin)
    tryagain = input("\n\n Press enter to try again, 'n' to stop\n")
    if tryagain == 'n':
        break