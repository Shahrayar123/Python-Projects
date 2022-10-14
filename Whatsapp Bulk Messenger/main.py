import pywhatkit

# # Send a WhatsApp Message to a Contact at 1:30 PM
# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

f = open("message.txt", "r")
message = f.read()
f.close()

numbers = []
f = open("Numbers.txt", "r")
for line in f.read().splitlines():
    if line.strip() != "":
        numbers.append(line.strip())
f.close()

total_number = len(numbers)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
delay = 30


input(
    style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
for idx, number in enumerate(numbers):
    number = number.strip()
    if number == "":
        continue
    print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx + 1), total_number, number) + style.RESET)
    pywhatkit.sendwhats_image(number, "Images/earth1.jpg", message,15,True,5)

    print(style.GREEN + 'Message sent to: ' + number + style.RESET)



# Send an Image to a Group with the Caption as Hello


# # Send an Image to a Contact with the no Caption
# pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")
#
# # Send a WhatsApp Message to a Group at 12:00 AM
# pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)
#
# # Send a WhatsApp Message to a Group instantly
# pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")
#
# # Play a Video on YouTube
# pywhatkit.playonyt("PyWhatKit")
