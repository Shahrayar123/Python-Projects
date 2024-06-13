MORSE_CODE_DICT = {'.-': 'A', '-...': 'B',
                   '-.-.': 'C', '-..': 'D', '.': 'E',
                   '..-.': 'F', '--.': 'G', '....': 'H',
                   '..': 'I', '.---': 'J', '-.-': 'K',
                   '.-..': 'L', '--': 'M', '-.': 'N',
                   '---': 'O', '.--.': 'P', '--.-': 'Q',
                   '.-.': 'R', '...': 'S', '-': 'T',
                   '..-': 'U', '...-': 'V', '.--': 'W',
                   '-..-': 'X', '-.--': 'Y', '--..': 'Z'}
# Solved characters is a string that holds what has been found already.
# Remaining characters holds dots and dashes that still need to be decoded.
def morsecode(solvedcharacters,remainingcharacters):
    if len(remainingcharacters) == 0:
        print(solvedcharacters)
        return
    elif len(remainingcharacters) == 1:
        print(solvedcharacters + MORSE_CODE_DICT[remainingcharacters])
        return
    for n in range(1,5):
        if remainingcharacters[0:n] in MORSE_CODE_DICT:
            morsecode(solvedcharacters + MORSE_CODE_DICT[remainingcharacters[0:n]],remainingcharacters[n:])
