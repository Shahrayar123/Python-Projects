# By Saad Khan

import colorama                         # For Adding Colors
import time                             # For Time Related Functions
import pyttsx3                          # For Speech
import sys,subprocess                   # For Working In Shell
from colorama import Fore,Back,Style    # For Adding Colors And Font Styles
from time import strftime

#colorama.init(autoreset=True)

voice=pyttsx3.init()
voice.setProperty('rate',150)

first_box=Fore.YELLOW+"1"
second_box=Fore.YELLOW+"2"
third_box=Fore.YELLOW+"3"
forth_box=Fore.YELLOW+"4"
fifth_box=Fore.YELLOW+"5"
sixth_box=Fore.YELLOW+"6"
seventh_box=Fore.YELLOW+"7"
eigth_box=Fore.YELLOW+"8"
ninth_box=Fore.YELLOW+"9"

def main_game_program():

    global first_box
    global second_box
    global third_box
    global forth_box
    global fifth_box
    global sixth_box
    global seventh_box
    global eigth_box
    global ninth_box

    first_box=Fore.YELLOW+"1"
    second_box=Fore.YELLOW+"2"
    third_box=Fore.YELLOW+"3"
    forth_box=Fore.YELLOW+"4"
    fifth_box=Fore.YELLOW+"5"
    sixth_box=Fore.YELLOW+"6"
    seventh_box=Fore.YELLOW+"7"
    eigth_box=Fore.YELLOW+"8"
    ninth_box=Fore.YELLOW+"9"

    day_and_date=strftime("%A, %D %B %Y")
    time_in_12h_format=strftime("%I:%M:%S %p")
    time_variable_for_greeting=int(strftime("%H"))

    welcome_intro="\n\n***** WELCOME TO TIC TAC TOE GAME *****"
    print(Fore.YELLOW + Back.CYAN + Style.BRIGHT + welcome_intro.center(75))
    print("\n\n")
    print(Fore.GREEN + day_and_date)
    print(Fore.GREEN + time_in_12h_format + "\n\n")

    playerx=input(Fore.MAGENTA + Back.YELLOW + "Who Wants To Be X : ")
    playero=input(Fore.MAGENTA + Back.YELLOW +  "Who Wants To Be O : ")
    print("\n")
    do_you_want_sound=input(Fore.RED + Back.WHITE + "Do You Want Sound [Y \ N] : ")
    print("\n\n")

    variable_for_greeting_by_name=f"{playerx}, and, {playero}, welcome to tic tac toe game."

    def input_for_speak_greeting(final_greetings):
        voice.say(final_greetings)
        voice.runAndWait()
        voice.stop()

    def speak_greetings():
        if (4<=time_variable_for_greeting<=12):
            variable_for_voice_greeting_according_to_time=f"Good Morning, {variable_for_greeting_by_name}"
            input_for_speak_greeting(variable_for_voice_greeting_according_to_time)
        elif (12<time_variable_for_greeting<18):
            variable_for_voice_greeting_according_to_time=f"Good Afternoon, {variable_for_greeting_by_name}"
            input_for_speak_greeting(variable_for_voice_greeting_according_to_time)
        elif (18<=time_variable_for_greeting<=22):
            variable_for_voice_greeting_according_to_time=f"Good Evening, {variable_for_greeting_by_name}"
            input_for_speak_greeting(variable_for_voice_greeting_according_to_time)
        elif (22<time_variable_for_greeting<=23 or 0<=time_variable_for_greeting<4):
            variable_for_voice_greeting_according_to_time=f"Hi, {variable_for_greeting_by_name}"
            input_for_speak_greeting(variable_for_voice_greeting_according_to_time)

    if (do_you_want_sound=="y" or do_you_want_sound=="Y" or do_you_want_sound=="yes" or do_you_want_sound=="Yes" or do_you_want_sound=="YES"):
            speak_greetings()
            
    def game_layout():
         print(Back.WHITE+Fore.GREEN+"....."+first_box+Fore.GREEN+"....."+"|"+"....."+second_box+Fore.GREEN+"....."+"|"+"....."+third_box+Fore.GREEN+".....")
         print(Back.WHITE+Fore.GREEN+"-----------------------------------")
         print(Back.WHITE+Fore.GREEN+"....."+forth_box+Fore.GREEN+"....."+"|"+"....."+fifth_box+Fore.GREEN+"....."+"|"+"....."+sixth_box+Fore.GREEN+".....")
         print(Back.WHITE+Fore.GREEN+"-----------------------------------")
         print(Back.WHITE+Fore.GREEN+"....."+seventh_box+Fore.GREEN+"....."+"|"+"....."+eigth_box+Fore.GREEN+"....."+"|"+"....."+ninth_box+Fore.GREEN+".....")

    class speak_turns:
        def playerx_speak_for_turn(speak_for_x_turn):
            voice.say(speak_for_x_turn)
            voice.runAndWait()
            voice.stop()
        def playero_speak_for_turn(speak_for_o_turn):
            voice.say(speak_for_o_turn)
            voice.runAndWait()
            voice.stop()
        def speak_for_invalid_option():
            voice.say("Enter A Valid Option.")
            voice.runAndWait()
            voice.stop()

    def playerx_turn():
        subprocess.run('cls' , shell=True)
        game_layout()
        if (do_you_want_sound=="y" or do_you_want_sound=="Y" or do_you_want_sound=="yes" or do_you_want_sound=="Yes" or do_you_want_sound=="YES"):
            speak_turns.playerx_speak_for_turn(f"{playerx}\'s turn")
        turnx=input(f"{playerx}\'s turn : ")
        global first_box
        global second_box
        global third_box
        global forth_box
        global fifth_box
        global sixth_box
        global seventh_box
        global eigth_box
        global ninth_box
        if (turnx=="1"):
            first_box=Fore.RED+"X"
        elif (turnx=="2"):
            second_box=Fore.RED+"X"
        elif (turnx=="3"):
            third_box=Fore.RED+"X"
        elif (turnx=="4"):
            forth_box=Fore.RED+"X"
        elif (turnx=="5"):
            fifth_box=Fore.RED+"X"
        elif (turnx=="6"):
            sixth_box=Fore.RED+"X"
        elif (turnx=="7"):
            seventh_box=Fore.RED+"X"
        elif (turnx=="8"):
            eigth_box=Fore.RED+"X"
        elif (turnx=="9"):
            ninth_box=Fore.RED+"X"
        else:
            if (do_you_want_sound=="y" or do_you_want_sound=="Y" or do_you_want_sound=="yes" or do_you_want_sound=="Yes" or do_you_want_sound=="YES"):
                speak_turns.speak_for_invalid_option()
            print(Fore.RED+"Enter A Valid Option.")
            playerx_turn()
        subprocess.run('cls' , shell=True)

    def playero_turn():
        subprocess.run('cls' , shell=True)
        game_layout()
        if (do_you_want_sound=="y" or do_you_want_sound=="Y" or do_you_want_sound=="yes" or do_you_want_sound=="Yes" or do_you_want_sound=="YES"):
            speak_turns.playero_speak_for_turn(f"{playero}\'s turn")
        turno=input(f"{playero}\'s turn : ")
        global first_box
        global second_box
        global third_box
        global forth_box
        global fifth_box
        global sixth_box
        global seventh_box
        global eigth_box
        global ninth_box
        if (turno=="1"):
            first_box=Fore.BLUE+"O"
        elif (turno=="2"):
            second_box=Fore.BLUE+"O"
        elif (turno=="3"):
            third_box=Fore.BLUE+"O"
        elif (turno=="4"):
            forth_box=Fore.BLUE+"O"
        elif (turno=="5"):
            fifth_box=Fore.BLUE+"O"
        elif (turno=="6"):
            sixth_box=Fore.BLUE+"O"
        elif (turno=="7"):
            seventh_box=Fore.BLUE+"O"
        elif (turno=="8"):
            eigth_box=Fore.BLUE+"O"
        elif (turno=="9"):
            ninth_box=Fore.BLUE+"O"
        else:
            if (do_you_want_sound=="y" or do_you_want_sound=="Y" or do_you_want_sound=="yes" or do_you_want_sound=="Yes" or do_you_want_sound=="YES"):
                speak_turns.speak_for_invalid_option()
            print(Fore.BLUE+"Enter A Valid Option.")
            playero_turn()
        subprocess.run('cls' , shell=True)

    def do_you_want_to_restart_game_function():
        subprocess.run('cls' , shell=True)
        if (do_you_want_sound=="y" or do_you_want_sound=="Y" or do_you_want_sound=="yes" or do_you_want_sound=="Yes" or do_you_want_sound=="YES"):
            voice.say("Do You Want To Restart Game, Type Y/yes or N/no")
            voice.runAndWait()
            voice.stop()
        do_you_want_to_restart_game=input(Back.WHITE+Fore.RED+"Do You Want To Restart Game [Y \ N] : ")
        if (do_you_want_to_restart_game=="y" or do_you_want_to_restart_game=="Y" or do_you_want_to_restart_game=="yes" or do_you_want_to_restart_game=="Yes" or do_you_want_to_restart_game=="YES"):
            if (do_you_want_sound=="y" or do_you_want_sound=="Y" or do_you_want_sound=="yes" or do_you_want_sound=="Yes" or do_you_want_sound=="YES"):
                voice.say("Restarting Game In 3 Seconds.")
                voice.runAndWait()
                voice.stop()
            print(Back.WHITE+Fore.RED+Style.BRIGHT+"Restarting Game In 3 Seconds.")
            time.sleep(3)
            main_game_program()
        elif(do_you_want_to_restart_game=="n" or do_you_want_to_restart_game=="N" or do_you_want_to_restart_game=="no" or do_you_want_to_restart_game=="No" or do_you_want_to_restart_game=="NO"):
            subprocess.run('cls' , shell=True)
            if (do_you_want_sound=="y" or do_you_want_sound=="Y" or do_you_want_sound=="yes" or do_you_want_sound=="Yes" or do_you_want_sound=="YES"):
                voice.say("Thank You !, Hope You Enjoyed!")
                voice.runAndWait()
                voice.stop()
            print(Back.BLACK+Fore.GREEN+"THANK YOU !!! \nHOPE YOU ENJOYED !")
            variable_to_stop_immediate_termination_of_shell=input()
            exit()
        else:
            if (do_you_want_sound=="y" or do_you_want_sound=="Y" or do_you_want_sound=="yes" or do_you_want_sound=="Yes" or do_you_want_sound=="YES"):
                voice.say("Enter A Valid Option.")
                voice.runAndWait()
                voice.stop()
            print(Back.WHITE+Fore.RED+"Enter A Valid Option.")
            do_you_want_to_restart_game_function()
    
    def playerx_wins_greetings_function():
        if (do_you_want_sound=="y" or do_you_want_sound=="Y" or do_you_want_sound=="yes" or do_you_want_sound=="Yes" or do_you_want_sound=="YES"):
            voice.say(f"{playerx} Wins, Congratulations")
            voice.runAndWait()
            voice.stop()
        print(Back.YELLOW+Fore.BLUE+f"{playerx} Wins\nCongratulations !!!")
        time.sleep(0.5)
        do_you_want_to_restart_game_function()

    def playero_wins_greetings_function():
        if (do_you_want_sound=="y" or do_you_want_sound=="Y" or do_you_want_sound=="yes" or do_you_want_sound=="Yes" or do_you_want_sound=="YES"):
            voice.say(f"{playero} Wins, Congratulations")
            voice.runAndWait()
            voice.stop()
        print(Back.YELLOW+Fore.RED+f"{playero} Wins\nCongratulations !!!")
        time.sleep(0.5)
        do_you_want_to_restart_game_function()
    
    i=0   
    while(True):

        playerx_turn()

        if (first_box==second_box==third_box==Fore.RED+"X") :
            playerx_wins_greetings_function()
        elif (forth_box==fifth_box==sixth_box==Fore.RED+"X") :
            playerx_wins_greetings_function()
        elif (seventh_box==eigth_box==ninth_box==Fore.RED+"X") :
            playerx_wins_greetings_function()
        elif (first_box==forth_box==seventh_box==Fore.RED+"X") :
            playerx_wins_greetings_function()
        elif (second_box==fifth_box==eigth_box==Fore.RED+"X") :
            playerx_wins_greetings_function()
        elif (third_box==sixth_box==ninth_box==Fore.RED+"X") :
            playerx_wins_greetings_function()
        elif (first_box==fifth_box==ninth_box==Fore.RED+"X") :
            playerx_wins_greetings_function()
        elif (third_box==fifth_box==seventh_box==Fore.RED+"X") :
            playerx_wins_greetings_function()

        playero_turn()

        if (first_box==second_box==third_box==Fore.BLUE+"O") :
            playero_wins_greetings_function()
        elif (forth_box==fifth_box==sixth_box==Fore.BLUE+"O") :
            playero_wins_greetings_function()
        elif (seventh_box==eigth_box==ninth_box==Fore.BLUE+"O") :
            playero_wins_greetings_function()
        elif (first_box==forth_box==seventh_box==Fore.BLUE+"O") :
            playero_wins_greetings_function()
        elif (second_box==fifth_box==eigth_box==Fore.BLUE+"O") :
            playero_wins_greetings_function()
        elif (third_box==sixth_box==ninth_box==Fore.BLUE+"O") :
            playero_wins_greetings_function()
        elif (first_box==fifth_box==ninth_box==Fore.BLUE+"O") :
            playero_wins_greetings_function()
        elif (third_box==fifth_box==seventh_box==Fore.BLUE+"O") :
            playero_wins_greetings_function()
            
        i=i+1
        if i==10:
            if (do_you_want_sound=="y" or do_you_want_sound=="Y" or do_you_want_sound=="yes" or do_you_want_sound=="Yes" or do_you_want_sound=="YES"):
                voice.say("Tie ! No One Wins.")
                voice.runAndWait()
                voice.stop()
            print(Back.YELLOW+Fore.GREEN+"Tie !!!\nNo One Wins.")
            do_you_want_to_restart_game_function()


main_game_program()
