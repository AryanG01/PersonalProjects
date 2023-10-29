from Questions import Questions

series_of_questions =[
    "What Colour are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What Colour are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What Colour are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

list_of_questions = [
    Questions(series_of_questions[0], 'a'),
    Questions(series_of_questions[1], 'c'),
    Questions(series_of_questions[2], 'b')
]

def MCQ(Question_Array):
    score = 0
    for question in Question_Array:
        answer = input(question.prompt + "Enter Your Answer: ")
        if answer == question.answer:
            score += 1
            print("Correct Answer!\n")
        else:
            print("Wrong Answer, the correct answer was " + question.answer + "\n")
    print("\nYou got " + str(score) + "/" + str(len(list_of_questions)) + " Correct")

MCQ(list_of_questions)