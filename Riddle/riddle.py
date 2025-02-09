import random
import collections

glob_list = collections.defaultdict(list)                    # a list to collect all correct values of anagram entered by user in backpack



def anagram(word01,solnword,qnword,n):                      # defining a function which checks ans entered by user and adds it to backpack if correcct
  s=0                                                       # s=0 if user enters wrong ans 0 is returned and added to score
  temp1="".join(sorted(word01))
  temp2="".join(sorted(solnword))
  if len(word01) !=n :
    print("number of letters do not match")                 
  elif word01==qnword:
      print("U typed the same thing")            
  else:
    if temp1==temp2:  
      if word01==solnword:
          print("you are correct\ncurrent backpack is:") 
          s+=1                                               # variable to update score value
          global glob_list
          glob_list[temp1].append(word01)
          glob_list[temp1].append(qnword) 
          print(*glob_list.values())
          
      else:
          print("u just typed random")
  return s                                                   # adding one to score if ans is correct and returning 


# Riddle game

riddles = {
    "I have cities but no houses, forests but no trees, and water but no fish. What am I?": "map",
    "I am always hungry, I must always be fed. The finger I touch, will soon turn red. What am I?": "Fire",
    "I am not alive, but I grow. I don't have lungs, but I need air. I don't have a mouth, but water kills me. What am I?": "Fire",
    "What has a heart that doesn't beat?": "Artichoke",
    "What is so fragile that saying its name breaks it?": "Silence",
    "The person who makes it, sells it. The person who buys it never uses it. What is it?": "coffin",
    "The more you take, the more you leave behind. What am I?": "footsteps"       # added more riddles
}

score = 0

riddle_keys = list(riddles.keys())  # Convert the dictionary keys into a list.

random.shuffle(riddle_keys)  # Shuffle the list of riddle keys.



for riddle_key in riddle_keys:
    print(riddle_key)
    user_answer = input("Answer: ").lower()
    if user_answer == riddles[riddle_key].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong answer. Correct answer: " + riddles[riddle_key])
print("\n"+str(score))        

# anagram game

print("\n\nLEVEL 2\n\n")

print("""An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
         typically using all the original letters exactly once.\n\n For example elbow and below\n""") # instructions to user about the game

answord1=["below","reactive","listen","flea","enraged","admirer"] # solution words
solutionword=["elbow","creative","silent","leaf","angered","married"] # question words (random not added)

for i in range(len(solutionword)):
   word1=input("Rearrange the letters of the word  -" +answord1[i] +"-   and form another meaningful word\n")
   score+=anagram(word1.lower(),solutionword[i],answord1[i],len(solutionword[i])) # word1 .lower is given so game is not case sensitive 
   print("next\n")        

print("Game over! Your score is: " + str(score))
