#This app will ask you questions
#Mark the answers
#And record the scores 
print("Welcome to the squid game,and answer the question")
name=input("Please enter your name :")
print("Hello, ",name)
score=0
print("Your score is", score,"Lets get started!!")

#ask the first question
answer=input("Question 1: Who was the last US president :").lower()

#check if the answer is correct
if answer=="donald trump":
    print("Correct")
    score=score+10
    print("Your score :",score)
else:
    score = score - 10
    print("Incorrect, Your score is ",score)
answer=input("Question 2: What is the name of the planet number 2 in solar system? :").lower()

#check if the answer is correct
if answer=="venus":
    score=score+10
    print("correct!")
    print("Your new score : ",score)
else:
    score=score-10
    print("incorrect!")
    print("Your new score :",score)
like=0
if like=="like":
    like=like+1
    