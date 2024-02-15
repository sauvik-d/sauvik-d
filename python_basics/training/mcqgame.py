from Question import Question

question_prompts = [
    "Who is the director of Inglorious Basterds?\na) Martin Scorsese\nb) Quentin Tarantino\nc) George Lukas\n"
]

questions = [
    Question(question_prompts[0], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1
    print("You got "+ str(score))


run_test(questions)
