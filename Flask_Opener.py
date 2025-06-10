from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def set_work():
    name = request.form.get('name', 'Guest')
    greeting = f"Hello, {name}!"
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)

from Quantize import *
Quantize = Quantize()
