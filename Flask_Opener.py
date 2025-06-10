from flask import Flask, render_template, request
from Quantize import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Interface.html')

@app.route('/quantize', methods=['POST'])
def set_work():
    maxRate = request.form.get('maxRange')
    minRate = request.form.get('minRange')
    sampleRate = request.form.get('sampleRate')
    bitRate = request.form.get('bitRate')
    analogVoltage = request.form.get('analogVoltage')  
    quantizedValue = Quantize(maxRate, minRate, sampleRate, bitRate, analogVoltage)
    greeting = f"Quantized Value: {quantizedValue}"
    return render_template('Interface.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)

