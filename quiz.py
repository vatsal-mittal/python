 from Question import Question

question_prompts = [
    "what is the color of apple?\n(a) red/green\n(b) yellow\n(c) purple\n\n",
    "what is the name of the largest ocean?\n(a) antlantic\n(b) artic\n(c) pacific\n\n",
    "what is my name?\n(a) raju\n(b) vatsal\n(c) rahul\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)

input("click enter to exit: ")