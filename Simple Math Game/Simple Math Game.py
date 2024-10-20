import random
import time
import easygui

score = 0
start_time = time.time()

for i in range(1,6):

    first_number = random.randint(1,10)
    second_number = random.randint(1,10)
    operators = ['+','-','/','%','*']
    selected_operator = random.choice(operators)

    message = "Problem",i,"->", first_number, selected_operator, second_number
    user_answer = easygui.enterbox(message,"Enter your answer:")
    
    if selected_operator == '+':
        result = first_number + second_number
        if result == eval(user_answer):
            score = score+1
        else:
            print("Answer is:-",result)
        
    elif selected_operator == '-':
        result = first_number - second_number
        if result == eval(user_answer):
            score = score+1
        else:
            print("Answer is:-",result)
            
    elif selected_operator == '/':
        result = round(first_number / second_number,1)
        if result == eval(user_answer):
            score = score+1
        else:
            print("Answer is:-",result)
            
    elif selected_operator == '%':
        result = first_number % second_number
        if result == eval(user_answer):
            score = score+1
        else:
            print("Answer is:-",result)

    elif selected_operator == '*':
        result = first_number * second_number
        if result == eval(user_answer):
            score = score+1
        else:
            print("Answer is:-",result)

end_time = time.time()
final_time = round(end_time - start_time,2)
result_message = (f"You have scored {score} points in {final_time} seconds.")
easygui.msgbox(result_message, "Result")
