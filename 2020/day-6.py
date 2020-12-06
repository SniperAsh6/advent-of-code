def input_to_group_answers(raw_input):
    group_answers = []
    group_answer = []
    for i, line in enumerate(raw_input):
        if line == "\n":
            if len(group_answer) > 0:
                group_answers.append(group_answer)
            group_answer = []
            continue
        group_answer.append(line.replace("\n", ""))
        if i == len(raw_input) - 1:
            group_answers.append(group_answer)
    return group_answers

def custom_customs(answers_input):
    yes_question_count = 0
    for group in answers_input:
        group_questions = []
        for individual in group:
            for answer in individual:
                if answer not in group_questions:
                    group_questions.append(answer)
        yes_question_count += len(group_questions)
    print(yes_question_count)

with open(r"2020/Input/day-6-puzzle.txt") as input_data_file:
    input_data = input_data_file.readlines()

answers_data = input_to_group_answers(input_data)
custom_customs(answers_data)
