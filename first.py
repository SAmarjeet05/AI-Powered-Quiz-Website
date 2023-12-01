from flask import Flask, render_template, request, redirect, url_for, send_file
from openai import OpenAI
import string
import random
from flask_googlecharts import GoogleCharts
from flask_googlecharts import PieChart
import csv
import os
client = OpenAI()

app = Flask('__name__')
charts = GoogleCharts(app)
my_chart = PieChart("my_chart")
my_chart = PieChart("my_chart", options={'title': 'Correct/Incorrect'})

'''name = "python"
age="26"
qualification="AIML Engineer"

list1=["Amarjeet Singh",18,"AIML Engineering"]

@app.route('/')
def isthe():
    return render_template("passtry.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html",name=list1[0],age=list1[1],ql=list1[2])

@app.route("/",methods=['POST'])
def passtry():
    name=request.form['name']
    age=request.form['age']
    dob=request.form['dateofbirth']
    return render_template("about.html",name=name,age=age,dob=dob)

if __name__=="__main__":
    app.run()'''


@app.route('/')
def starting_page():
    return render_template("starting_page.html")

@app.route('/topic_page')
def topic_page():
    return render_template("topic_page.html")

@app.route('/num_question_page', methods=['POST'])
def num_question_page():
    global topic
    global subtopic
    topic=request.form['topic']
    return render_template("num_question_page.html")

@app.route('/quiz_generating_page', methods=['POST'])
def quiz_generating_page():
    global number
    global answers
    global questions
    global answers
    global correct_answers
    global answers_nested_list
    global dictionary_nested_list
    global question_answer2
    global code
    global new_question_answers

    questions = []
    answers = []
    correct_answers = []
    answers_nested_list = []
    dictionary_nested_list = []
    question_answer2 = []


    upper_letters=string.ascii_uppercase
    lower_letters=string.ascii_lowercase
    digit=string.digits
    all = upper_letters + lower_letters + digit
    length=6
    code="".join(random.sample(all,length))
    print(code)

    number=request.form['number']
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are an education assistant, skilled in generating quiz questions on any topic"},
            {"role": "system", "content": "Ask {} multiple choice question in the following form but of {}: What is the capital of France?. A) Berlin B) Rome C) Paris (correct) D) Amsterdam".format(number,topic)}
        ]
    )
    question_answers1 = completion.choices[0].message

    question_answers = str(question_answers1)

    #Removing extra charactors
    length=len(question_answers)
    question_answers = question_answers[31:length-57]

    #Getting a list of questiona and answers
    new_question_answers = question_answers.split("\\n")

    for i in new_question_answers:
        if ("?" in i) == True or (":" in i) == True:
            questions.append(i)
        if ("A)" in i) == True or ("B)" in i) == True or ("C)" in i) == True or ("D)" in i) == True:
            if ("(correct)" in i) == True:
                correct_answers.append(i[:-10])
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

    name="quizcodes"+"/"+code+".csv"
    print(correct_answers)
    print(answers)
    with open(name,'a',newline='',encoding="utf-8") as f:
        data = csv.writer(f)
        datalist = [questions,answers,correct_answers,[topic]]
        #data.writerows(datalist)
        for i in datalist:
            data.writerow(i)


    k = answers_nested_list
    print(questions)
    print(len(questions))

    if len(questions)==3:
        return render_template("quiz_generating_page3.html",code=code,topic=topic,question1=questions[0],question2=questions[1],question3=questions[2],option11=answers[0],option12=answers[1],option13=answers[2],option14=answers[3],option21=answers[4],option22=answers[5],option23=answers[6],option24=answers[7],option31=answers[8],option32=answers[9],option33=answers[10],option34=answers[11])
    
    if len(questions)==5:
        return render_template("quiz_generating_page5.html",code=code,topic=topic,question1=questions[0],question2=questions[1],question3=questions[2],question4=questions[3],question5=questions[4],option11=answers[0],option12=answers[1],option13=answers[2],option14=answers[3],option21=answers[4],option22=answers[5],option23=answers[6],option24=answers[7],option31=answers[8],option32=answers[9],option33=answers[10],option34=answers[11],option41=answers[12],option42=answers[13],option43=answers[14],option44=answers[15],option51=answers[16],option52=answers[17],option53=answers[18],option54=answers[19])
    
    if len(questions)==10:
        return render_template("quiz_generating_page10.html",code=code,topic=topic,question1=questions[0],question2=questions[1],question3=questions[2],question4=questions[3],question5=questions[4],question6=questions[5],question7=questions[6],question8=questions[7],question9=questions[8],question10=questions[9],option11=answers[0],option12=answers[1],option13=answers[2],option14=answers[3],option21=answers[4],option22=answers[5],option23=answers[6],option24=answers[7],option31=answers[8],option32=answers[9],option33=answers[10],option34=answers[11],option41=answers[12],option42=answers[13],option43=answers[14],option44=answers[15],option51=answers[16],option52=answers[17],option53=answers[18],option54=answers[19],option61=answers[20],option62=answers[21],option63=answers[22],option64=answers[23],option71=answers[24],option72=answers[25],option73=answers[26],option74=answers[27],option81=answers[28],option82=answers[29],option83=answers[30],option84=answers[31],option91=answers[32],option92=answers[33],option93=answers[34],option94=answers[35],option101=answers[36],option102=answers[37],option103=answers[38],option104=answers[39])

    if len(questions)==15:
        return render_template("quiz_generating_page15.html",code=code,topic=topic,question1=questions[0],question2=questions[1],question3=questions[2],question4=questions[3],question5=questions[4],question6=questions[5],question7=questions[6],question8=questions[7],question9=questions[8],question10=questions[9],question11=questions[10],question12=questions[11],question13=questions[12],question14=questions[13],question15=questions[14],option11=answers[0],option12=answers[1],option13=answers[2],option14=answers[3],option21=answers[4],option22=answers[5],option23=answers[6],option24=answers[7],option31=answers[8],option32=answers[9],option33=answers[10],option34=answers[11],option41=answers[12],option42=answers[13],option43=answers[14],option44=answers[15],option51=answers[16],option52=answers[17],option53=answers[18],option54=answers[19],option61=answers[20],option62=answers[21],option63=answers[22],option64=answers[23],option71=answers[24],option72=answers[25],option73=answers[26],option74=answers[27],option81=answers[28],option82=answers[29],option83=answers[30],option84=answers[31],option91=answers[32],option92=answers[33],option93=answers[34],option94=answers[35],option101=answers[36],option102=answers[37],option103=answers[38],option104=answers[39],option111=answers[40],option112=answers[41],option113=answers[42],option114=answers[43],option121=answers[44],option122=answers[45],option123=answers[46],option124=answers[47],option131=answers[48],option132=answers[49],option133=answers[50],option134=answers[51],option141=answers[52],option142=answers[53],option143=answers[54],option144=answers[55],option151=answers[56],option152=answers[57],option153=answers[58],option154=answers[59])

    #return render_template("quiz_generating_page.html",subtopic=subtopic,question1=questions[0],question2=questions[1],question3=questions[2],option11=options1[0],option12=options1[1],option13=options1[2],option14=options1[3],option21=options1[4],option22=options1[4],option23=options1[6],option24=options1[7],option31=options1[8],option32=options1[9],option33=options1[10],option34=options1[11])

@app.route('/result', methods=['POST'])
def result():
    global score
    score=0

    name="quizcodes"+"/"+code+".csv"
    readata1=[]
    with open(name,'r')as f:
        data=csv.reader(f)
        for i in data:
            readata1.append(i)
    canswers=readata1[2]
    code_questions=readata1[0]
    print(len(code_questions))

    if len(code_questions)==3:
        answer1 = request.form['question1']
        answer2 = request.form['question2']
        answer3 = request.form['question3']
        for i in canswers:
            if (answer1 in i) == True or (answer2 in i) == True or (answer3 in i) == True:
                score=score+1
    if len(code_questions)==5:
        answer1 = request.form['question1']
        answer2 = request.form['question2']
        answer3 = request.form['question3']
        answer4 = request.form['question4']
        answer5 = request.form['question5']
        for i in canswers:
            if (answer1 in i) == True or (answer2 in i) == True or (answer3 in i) == True or (answer4 in i) == True or (answer5 in i) == True:
                score=score+1
    if len(code_questions)==10:
        answer1 = request.form['question1']
        answer2 = request.form['question2']
        answer3 = request.form['question3']
        answer4 = request.form['question4']
        answer5 = request.form['question5']
        answer6 = request.form['question6']
        answer7 = request.form['question7']
        answer8 = request.form['question8']
        answer9 = request.form['question9']
        answer10 = request.form['question10']
        print(answer1,answer2,answer3,answer4,answer5,answer6,answer7,answer8,answer9,answer10)

        for i in canswers:
            if (answer1 in i) == True or (answer2 in i) == True or (answer3 in i) == True or (answer4 in i) == True or (answer5 in i) == True or (answer6 in i) == True or (answer7 in i) == True or (answer8 in i) == True or (answer9 in i) == True or (answer10 in i) == True:
                score=score+1

    if len(code_questions)==15:
        answer1 = request.form['question1']
        answer2 = request.form['question2']
        answer3 = request.form['question3']
        answer4 = request.form['question4']
        answer5 = request.form['question5']
        answer6 = request.form['question6']
        answer7 = request.form['question7']
        answer8 = request.form['question8']
        answer9 = request.form['question9']
        answer10 = request.form['question10']
        answer11 = request.form['question11']
        answer12 = request.form['question12']
        answer13 = request.form['question13']
        answer14 = request.form['question14']
        answer15 = request.form['question15']
        for i in canswers:
            if (answer1 in i) == True or (answer2 in i) == True or (answer3 in i) == True or (answer4 in i) == True or (answer5 in i) == True or (answer6 in i) == True or (answer7 in i) == True or (answer8 in i) == True or (answer9 in i) == True or (answer10 in i) == True or (answer11 in i) == True or (answer12 in i) == True or (answer13 in i) == True or (answer14 in i) == True or (answer15 in i) == True:
                score=score+1

    #print(canswers)
    print(answer1,answer2,answer3)
    print(correct_answers)
    length=len(canswers)
    incorrect = int(length)-score
    print(score)
    print(incorrect)
    piedata = {'Correct':score,'Incorrect':incorrect}
    print(piedata)
    #my_chart = PieChart("my_chart", options={'title': 'Corret/Incorrect'}, data=data)
    return render_template("result_page.html",score=score,incorrect=incorrect,piedata=piedata)

@app.route('/code_quiz_result_page',methods=['POST'])
def code_quiz_result():
    global score
    name="quizcodes"+"/"+code_value+".csv"
    readata1=[]
    with open(name,'r')as f:
        data=csv.reader(f)
        for i in data:
            readata1.append(i)
    canswers=readata1[2]
    code_questions=readata1[0]

    score=0
    if len(code_questions)==3:
        answer1 = request.form['question1']
        answer2 = request.form['question2']
        answer3 = request.form['question3']
        for i in canswers:
            if (answer1 in i) == True or (answer2 in i) == True or (answer3 in i) == True:
                score=score+1
    if len(code_questions)==5:
        answer1 = request.form['question1']
        answer2 = request.form['question2']
        answer3 = request.form['question3']
        answer4 = request.form['question4']
        answer5 = request.form['question5']
        for i in canswers:
            if (answer1 in i) == True or (answer2 in i) == True or (answer3 in i) == True or (answer4 in i) == True or (answer5 in i) == True:
                score=score+1
    if len(code_questions)==10:
        answer1 = request.form['question1']
        answer2 = request.form['question2']
        answer3 = request.form['question3']
        answer4 = request.form['question4']
        answer5 = request.form['question5']
        answer6 = request.form['question6']
        answer7 = request.form['question7']
        answer8 = request.form['question8']
        answer9 = request.form['question9']
        answer10 = request.form['question10']
        for i in canswers:
            if (answer1 in i) == True or (answer2 in i) == True or (answer3 in i) == True or (answer4 in i) == True or (answer5 in i) == True or (answer6 in i) == True or (answer7 in i) == True or (answer8 in i) == True or (answer9 in i) == True or (answer10 in i) == True:
                score=score+1
    if len(code_questions)==15:
        answer1 = request.form['question1']
        answer2 = request.form['question2']
        answer3 = request.form['question3']
        answer4 = request.form['question4']
        answer5 = request.form['question5']
        answer6 = request.form['question6']
        answer7 = request.form['question7']
        answer8 = request.form['question8']
        answer9 = request.form['question9']
        answer10 = request.form['question10']
        answer11 = request.form['question11']
        answer12 = request.form['question12']
        answer13 = request.form['question13']
        answer14 = request.form['question14']
        answer15 = request.form['question15']
        for i in canswers:
            if (answer1 in i) == True or (answer2 in i) == True or (answer3 in i) == True or (answer4 in i) == True or (answer5 in i) == True or (answer6 in i) == True or (answer7 in i) == True or (answer8 in i) == True or (answer9 in i) == True or (answer10 in i) == True or (answer11 in i) == True or (answer12 in i) == True or (answer13 in i) == True or (answer14 in i) == True or (answer15 in i) == True:
                score=score+1
    #print(canswers)
    print(answer1,answer2,answer3)
    length=len(canswers)
    incorrect = int(length)-score
    print(score)
    print(incorrect)
    piedata = {'Correct':score,'Incorrect':incorrect}
    print(piedata)
    name="quizcoderesults/"+code_value+".csv"
    edata=[fname,score]
    with open(name,'a',newline='') as f:
        enter=csv.writer(f)
        enter.writerow(edata)
    #my_chart = PieChart("my_chart", options={'title': 'Corret/Incorrect'}, data=data)
    return render_template("result_page.html",score=score,incorrect=incorrect,piedata=piedata)


@app.route('/enter_code_page')
def enter_code_page():
    return render_template("enter_code_page.html")


@app.route('/code_quiz_page',methods=['POST'])
def code_quiz_page():
    global code_value
    global fname
    code_value = request.form['code_value']
    fname = request.form['fname']

    readata_list = []
    name = "quizcodes"+"/"+code_value+".csv"
    with open(name,'r') as f:
        readata = csv.reader(f)
        for i in readata:
            readata_list.append(i)

    questions=readata_list[0]
    answers=readata_list[1]
    correct_answers=readata_list[2]
    topic=readata_list[3][0]
    print(readata_list)
    if len(questions)==3:
        return render_template("code_quiz_generating_page3.html",topic=topic,question1=questions[0],question2=questions[1],question3=questions[2],option11=answers[0],option12=answers[1],option13=answers[2],option14=answers[3],option21=answers[4],option22=answers[5],option23=answers[6],option24=answers[7],option31=answers[8],option32=answers[9],option33=answers[10],option34=answers[11])
    
    if len(questions)==5:
        return render_template("code_quiz_generating_page5.html",topic=topic,question1=questions[0],question2=questions[1],question3=questions[2],question4=questions[3],question5=questions[4],option11=answers[0],option12=answers[1],option13=answers[2],option14=answers[3],option21=answers[4],option22=answers[5],option23=answers[6],option24=answers[7],option31=answers[8],option32=answers[9],option33=answers[10],option34=answers[11],option41=answers[12],option42=answers[13],option43=answers[14],option44=answers[15],option51=answers[16],option52=answers[17],option53=answers[18],option54=answers[19])
    
    if len(questions)==10:
        return render_template("code_quiz_generating_page10.html",topic=topic,question1=questions[0],question2=questions[1],question3=questions[2],question4=questions[3],question5=questions[4],question6=questions[5],question7=questions[6],question8=questions[7],question9=questions[8],question10=questions[9],option11=answers[0],option12=answers[1],option13=answers[2],option14=answers[3],option21=answers[4],option22=answers[5],option23=answers[6],option24=answers[7],option31=answers[8],option32=answers[9],option33=answers[10],option34=answers[11],option41=answers[12],option42=answers[13],option43=answers[14],option44=answers[15],option51=answers[16],option52=answers[17],option53=answers[18],option54=answers[19],option61=answers[20],option62=answers[21],option63=answers[22],option64=answers[23],option71=answers[24],option72=answers[25],option73=answers[26],option74=answers[27],option81=answers[28],option82=answers[29],option83=answers[30],option84=answers[31],option91=answers[32],option92=answers[33],option93=answers[34],option94=answers[35],option101=answers[36],option102=answers[37],option103=answers[38],option104=answers[39])

    if len(questions)==15:
        return render_template("code_quiz_generating_page15.html",topic=topic,question1=questions[0],question2=questions[1],question3=questions[2],question4=questions[3],question5=questions[4],question6=questions[5],question7=questions[6],question8=questions[7],question9=questions[8],question10=questions[9],question11=questions[10],question12=questions[11],question13=questions[12],question14=questions[13],question15=questions[14],option11=answers[0],option12=answers[1],option13=answers[2],option14=answers[3],option21=answers[4],option22=answers[5],option23=answers[6],option24=answers[7],option31=answers[8],option32=answers[9],option33=answers[10],option34=answers[11],option41=answers[12],option42=answers[13],option43=answers[14],option44=answers[15],option51=answers[16],option52=answers[17],option53=answers[18],option54=answers[19],option61=answers[20],option62=answers[21],option63=answers[22],option64=answers[23],option71=answers[24],option72=answers[25],option73=answers[26],option74=answers[27],option81=answers[28],option82=answers[29],option83=answers[30],option84=answers[31],option91=answers[32],option92=answers[33],option93=answers[34],option94=answers[35],option101=answers[36],option102=answers[37],option103=answers[38],option104=answers[39],option111=answers[40],option112=answers[41],option113=answers[42],option114=answers[43],option121=answers[44],option122=answers[45],option123=answers[46],option124=answers[47],option131=answers[48],option132=answers[49],option133=answers[50],option134=answers[51],option141=answers[52],option142=answers[53],option143=answers[54],option144=answers[55],option151=answers[56],option152=answers[57],option153=answers[58],option154=answers[59])

    #return render_template("quiz_generating_page3.html",topic=topic,question1=questions[0],question2=questions[1],question3=questions[2],option11=answers[0],option12=answers[1],option13=answers[2],option14=answers[3],option21=answers[4],option22=answers[5],option23=answers[6],option24=answers[7],option31=answers[8],option32=answers[9],option33=answers[10],option34=answers[11])




if __name__=="__main__":
    app.debug = True
    app.run()