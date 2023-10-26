SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #symbols included in the cipher
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt')
    choice = input('> ')
    if choice.lower().startswith('e'):
        mode = 'encrypt'
        break
    if choice.lower().startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter e or d\n')

while True:
    maxKey = len(SYMBOLS) - 1
    print('Enter a key')
    response = input('> ')
    if not response.isdecimal():
        print('Enter numeric key')
        response = input('> ')
    if 0 <= int(response) <= maxKey:
        key = int(response)
        break


print(f'Enter the text to {mode}')
text = input('> ').upper()

translated_text = ''

for char in text: 
    if char in SYMBOLS:
        num = SYMBOLS.find(char)
        if mode == 'encrypt':
            num += key
        if mode == 'decrypt':
            num -= key
        if num >= maxKey:
            num -= maxKey
        elif num < 0:
            num += maxKey

        translated_text += SYMBOLS[num]
    else:
        translated_text += char

print('\n', translated_text)
