from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def head():
    return render_template('index.html', number1 =1250 , number2 = 60000)

@app.route('/mult')
def number():
    var1, var2 = 15000, 2
    return render_template('body.html', num1 = var1, num2 = var2, multiplication = var1*var2)







if __name__ == '__main__':
    app.run(debug=True)