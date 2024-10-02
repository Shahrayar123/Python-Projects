# Dictionary mapping English letters to Galactic Alphabet
galactic_alphabet = {
    'a': 'ᔑ', 'b': 'ʖ', 'c': 'ᓵ', 'd': '↸', 'e': 'ᒷ', 'f': '⎓', 'g': '⊣', 'h': '⍑', 'i': '╎', 'j': '⋮', 
    'k': 'ꖌ', 'l': 'ꖎ', 'm': 'ᒲ', 'n': 'リ', 'o': '𝙹', 'p': '!¡', 'q': 'ᑑ', 'r': '∷', 's': 'ᓭ', 't': 'ℸ', 
    'u': '⚍', 'v': '⍊', 'w': '∴', 'x': ' ̇/', 'y': '||', 'z': '⨅', ' ': ' '
}

# Function to convert English to Galactic alphabet
def convert_to_galactic(sentence):
    galactic_sentence = ""
    for char in sentence.lower():
        if char in galactic_alphabet:
            galactic_sentence += galactic_alphabet[char]
        else:
            galactic_sentence += char  # Keep non-alphabet characters like punctuation unchanged
    return galactic_sentence

# Get user input
english_sentence = input("Enter a sentence in English: ")

# Output the converted sentence
galactic_sentence = convert_to_galactic(english_sentence)
print("Sentence in Galactic Alphabet:", galactic_sentence)
