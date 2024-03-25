from flask import Flask,render_template,request
import random
app = Flask(__name__)
@app.route('/')
def webpage():
    return render_template('webpage.html')
@app.route('/play',methods=["POST"])
def play():
    computer_choice = random.randint(0, 2)
    user_choice = int(request.form['choice'])
    choices = ['Rock','Paper','Scissors']
    result=""
    computer_point = 0
    your_point = 0
    if computer_choice == user_choice:
        result = "Draw"
        computer_point = 0
        your_point = 0
    elif computer_choice == 0 and user_choice == 2:
        result ="Computer wins!!"
        computer_point = 1
        your_point = 0
    elif computer_choice == 2 and user_choice == 0:
        result ="You win!!"
        computer_point = 0
        your_point = 1
    elif user_choice < computer_choice:
        result ="Computer wins!!"
        computer_point = 1
        your_point = 0
    elif user_choice > computer_choice:
        result ="You win!!"
        computer_point = 0
        your_point = 1

    computer_choice_text = choices[computer_choice]
    user_choice_text = choices[user_choice]
    return render_template('result.html', result=result, user_choice=user_choice_text,
                           computer_choice=computer_choice_text,computer_point=computer_point,your_point=your_point)


if __name__ == '__main__':
    app.run(debug=True)