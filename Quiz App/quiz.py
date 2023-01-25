#This app will ask you questions
#Mark the answers
#And record the scores 
print("Welcome to the squid game,and answer the question")
name=input("Please enter your name :")
print("Hello, ",name)
score=0
print("Your score is", score,"Lets get started!!")
answer=input("Question 1: Who was the last US president :").lower()
if answer=="donald trump":
    print("Correct")
    score=score+10
    print("Your score :",score)
else:
    print("Incorrect, Your score is ",score)
answer=input("Question 2: ")