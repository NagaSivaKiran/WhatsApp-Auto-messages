from flask import Flask, render_template, request, redirect, url_for
import pywhatkit
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    phone_number = request.form['phone_number']
    message = request.form['message']
    hour = int(request.form['hour'])
    minute = int(request.form['minute'])

    # Calculate current time
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    # Calculate call time in minutes
    call_time_minutes = hour * 60 + minute

    # Calculate current time in minutes
    current_time_minutes = current_hour * 60 + current_minute

    # Calculate wait time (difference between call time and current time)
    wait_time_minutes = call_time_minutes - current_time_minutes

    # Check if call time is in the future (greater than wait time)
    if wait_time_minutes >= 0:
        try:
            pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
            return 'Message sent successfully!'
        except Exception as e:
            return f'Error: {str(e)}'
    else:
        return 'Error: Call Time must be greater than or equal to the current time.'

if __name__ == '__main__':
    app.run(port=1234, debug=True)
