#Import random module
import random

#Variable: Participant name
name = "Fred"

#Variable: Participant question
question = "Will I get a promotion this year?"

#Answer variable
answer = ""

#Declaring a variable called random and assigning it function to select a random number within a set range of numbers
random_number = random.randint(1, 9)

#Print randomly generated number
#print(random_number)

#if/elif/else statement to assign answers to specific numbers
if random_number == 1:
   answer = "Yes, definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

#print(answer)

#User input sequence:
print(name + " asks: " + question)

print("Magic 8-Balls answer: " + answer)
