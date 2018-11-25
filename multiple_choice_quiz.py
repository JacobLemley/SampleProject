from Question import Question

print("================Multiple Choice Quiz================\n")

#lets create an array of question prompts
question_prompts = [
    "\nWhat color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "\nWhat color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "\nWhat color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]


#this is an array of Question objects that contain a prompt and a correct answer
questions = [
    Question(question_prompts[0], "a"),     #this creates a Question object with the prompt from the 0 index of the earlier array and the correct answer of "a"
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

#now lets make a function to run the test and keep track of our score
def run_test(questions):
    score = 0 #sets the score to 0
    for question in questions :   #for loop that goes through each index in the questions array above
        answer = input(question.prompt)         #for the current index in the questions array, the promt is used then the input is compared with the answer attribute that was passed in when the object was made
        if answer.lower() == question.answer :
            score += 1
    print("\nYou got " + str(score) + "/" + str(len(questions)) + " questions correct.")

run_test(questions)

print("\n================Multiple Choice Quiz================")
