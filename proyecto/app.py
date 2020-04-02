from flask import Flask, render_template, request, redirect, url_for 
import leds

app = Flask(__name__)

@app.route('/')
def index():
      return render_template('index.html')

@app.route('/Mojito',methods=['POST'])
def Mojito():
      if request.method == 'POST':
            pass
      return redirect(url_for('index'))

@app.route('/Vodka',methods=['POST'])
def Vodka():
      if request.method == 'POST':
            pass
      return redirect(url_for('index'))

@app.route('/Piña_colada',methods=['POST'])
def Piña_colada():
      if request.method == 'POST':
            pass
      return redirect(url_for('index'))
@app.route('/Izquierda',methods=['POST'])
def Izquierda():
      if request.method == 'POST':
            leds.led.led1.on()
      return redirect(url_for('index'))

@app.route('/Ariba',methods=['POST'])
def Ariba():
      if request.method == 'POST':
            leds.led.led2.on()
      return redirect(url_for('index'))

@app.route('/Derecha',methods=['POST'])
def Derecha():
      if request.method == 'POST':
            leds.led.led3.on()
      return redirect(url_for('index'))

@app.route('/Stop',methods=['POST'])
def Stop():
      if request.method == 'POST':
            leds.led.off()
      return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")