import pywhatkit as pwk # You need to install this using pip install pywhatkit
def main(): # main function for taking input and using pywhatkit builtin function
    videoName = input("Search: ")
    pwk.playonyt(videoName) 
    
# calling of main function in exception handling block
try:
    main()
except:
    print("An unexpected error occurred")
finally:
    print("Script closed")
