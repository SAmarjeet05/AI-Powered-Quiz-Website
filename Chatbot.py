from openai import OpenAI

client = OpenAI()
topic = "maths"
number = "10"

completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are an education assistant, skilled in generating quiz questions on any topic"},
        {"role": "system", "content": "Ask {} multiple choice question in the following form but of {}: What is the capital of France?. A) Berlin B) Rome C) Paris (correct) D) Amsterdam".format(number,topic)}
    ]
)

question_answers1 = completion.choices[0].message

question_answers = str(question_answers1)

questions = []
dictionary_nested_list = []
answers = []
correct_answers = []
answers_nested_list = []
question_answer2 = []
length=len(question_answers)
question_answers = question_answers[31:length-57]
new_question_answers = question_answers.split("\\n")
print(new_question_answers)

for i in new_question_answers:
    if ("?" in i) == True or (":" in i) == True:
        questions.append(i)
    if ("A)" in i) == True or ("B)" in i) == True or ("C)" in i) == True or ("D)" in i) == True:
        if ("correct" in i) == True:
            correct_answers.append(i)
            answers.append(i[:-10])
        else:
            answers.append(i)   

for j in range(0,len(questions)):
    answers_nested_list.append([])
    dictionary_nested_list.append({})

for i in answers:
    for k in range(0,len(answers_nested_list)):
        if len(answers_nested_list[k])!=4:
            if any(i in sl for sl in answers_nested_list)==True:
                continue
            else:
                answers_nested_list[k].append(i)

for i in questions:
    for k in range(0,len(answers_nested_list)):
        if len(answers_nested_list[k])!=5:
            if any(i in sl for sl in answers_nested_list)==True:
                continue
            else:
                answers_nested_list[k].insert(0,i)

for i in answers_nested_list:
    for keys in range(1,6):
        for j in i:
            for k in range(0,len(dictionary_nested_list)):
                if len(dictionary_nested_list[k]) != 5:
                    if any(j in d.values() for d in dictionary_nested_list) == True:
                        continue
                    else:
                        dictionary_nested_list[k][keys] = j

#print(questions)
#print(correct_answers)
#print(answers)
print(answers_nested_list)
#print(dictionary_nested_list)