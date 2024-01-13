import random
import collections

glob_list = collections.defaultdict(list) # a list to collect all correct values of anagram entered by user in backpack



def anagram(word01,solnword,qnword,n):       
  s=0
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
          s+=1        
          global glob_list
          glob_list[temp1].append(word01)
          glob_list[temp1].append(qnword) 
          print(*glob_list.values())
          
      else:
          print("u just typed random")
  return s 


# Riddle game

riddles = {
    "I have cities but no houses, forests but no trees, and water but no fish. What am I?": "A map",
    "I am always hungry, I must always be fed. The finger I touch, will soon turn red. What am I?": "Fire",
    "I am not alive, but I grow. I don't have lungs, but I need air. I don't have a mouth, but water kills me. What am I?": "Fire",
    "What has a heart that doesn't beat?": "Artichoke",
    "What is so fragile that saying its name breaks it?": "Silence"
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


print("\n\nLEVEL 2\n\n")

print("""An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
         typically using all the original letters exactly once. For example elbow and below""")

answord1=["below","reactive","listen","flea","enraged","admirer"]
solutionword=["elbow","creative","silent","leaf","angered","married"]

for i in range(len(solutionword)):
   word1=input("Rearrange the letters of the word  -" +answord1[i] +"-   and form another meaningful word\n")
   score+=anagram(word1.lower(),solutionword[i],answord1[i],len(solutionword[i]))
   print("next\n")        

print("Game over! Your score is: " + str(score))
