from flask import Flask, render_template, request
import cv2
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
correct_password = "secure123"
attempt_counter = 0

def capture_photo(filename="captured_image.jpg"):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(filename, frame)
    cam.release()

def send_email(image_path):
    msg = EmailMessage()
    msg['Subject'] = 'Security Alert: Unauthorized Login Attempt'
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = 'recipient_email@gmail.com'
    msg.set_content('More than 3 incorrect login attempts detected.')

    with open(image_path, 'rb') as f:
        img_data = f.read()
        msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename='intruder.jpg')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('your_email@gmail.com', 'your_app_password')  # Use app password
        smtp.send_message(msg)

@app.route('/', methods=['GET', 'POST'])
def login():
    global attempt_counter
    message = ""

    if request.method == 'POST':
        password = request.form['password']
        if password == correct_password:
            message = "Access Granted"
            attempt_counter = 0
        else:
            attempt_counter += 1
            message = f"Incorrect password. Attempt {attempt_counter}"
            if attempt_counter > 3:
                capture_photo()
                send_email("captured_image.jpg")
                message = "Too many attempts. Alert sent!"

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
