'''import openai
from flask import request
from flask import Flask, render_template
from form import signupform

quiz=[]
quiz2=[]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('topic_page.html')
    quiz_result = False
    if request.method == 'POST':
        form = request.form
        quiz_result = quiz_generate(subtopic,number)
    
    return render_template('topic_page.html', quiz_result=quiz_result)

@app.route('/topic',method=['POST'])
def quiz_topic_value():
    global subtopic
    form=signupform()
    if form.is_submitted():
        subtopic=request.form['subtopic']

@app.route('/number',method=['POST'])
def quiz():
    global number
    form=signupform()
    if form.is_submitted():
        number=request.form['number']
        openai.api_key="your api no."
        prompt=f"Ask another multiple choice question in the following form but of {subtopic}: What is the capital of France? A) Berlin; B) Rome; C) Paris (correct); D) Amsterdam"

        response=openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=1,
        )
        
        question_and_answer = response["choices"][0]["text"]
        lines = question_and_answer.strip().split("?")
        options = lines[1].split(";")
        question = lines[0]
        answers = options[0:4]
        quiz.append(question_and_answer)
        quiz2.append(answers)
        return render_template('quiz_generating_page.html', ques=question , options=options)
    #print(question_and_answer)
    

    #return list

@app.route('/test', method=['POST'])
def test():
    output = request.get_json()
    print(output)

    result = json.loads(output)
    print(result)
    return result

if __name__=="__main__":
    app.run(debug=True)'''