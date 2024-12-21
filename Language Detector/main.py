# Language Detector
from langdetect import detect

# Detecting languages from input text
language1 = detect('¿Qué te gusta hacer')  
language2 = detect('Nyasae no omuya') 

# Mapping of language codes to human-readable names
language_mapping = {
    'es': 'Spanish',
    'en': 'English',
    'sw': 'Swahili',
    'ek': 'Kisii'  
}

# Print the detected language in a more user-friendly format
print(f'This is the {language_mapping.get(language1, language1)} language shortened by: {language1}')
print(f'This is the {language_mapping.get(language2, language2)} language shortened by: {language2}')
