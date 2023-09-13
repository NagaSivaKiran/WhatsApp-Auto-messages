
from flask import Flask, render_template, request, redirect, url_for
import pywhatkit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    phone_number = request.form['phone_number']
    message = request.form['message']
    hour = int(request.form['hour'])
    minute = int(request.form['minute'])

    try:
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
        return 'Message sent successfully!'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run( port=1234 , debug=True)
