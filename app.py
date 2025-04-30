from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__, static_folder='static')

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'stancilsdev@gmail.com' # Replace with your email
app.config['MAIL_PASSWORD'] = 'icec tsrg ujca biak' # Use your Gmail app password
app.config['MAIL_DEFAULT_SENDER'] = 'stancilsdev@gmail.com'

mail = Mail(app)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit-reflection', methods=["POST"])
def submit_reflection():
    message = request.form.get("message")
    if message:
        try:
            msg = Message("New Wisdom Shared via The Soul Scrolls",
                          recipients=["stancilsdev@gmail.com"])
            msg.body = f"Message from a visitor:\n\n{message}"
            mail.send(msg)
            return redirect(url_for("blog", success='true'))
        except Exception as e:
            print("Error sending email:", e)
            return redirect(url_for("blog", error='true'))
    return redirect(url_for("blog", error='true'))

@app.route("/submit-contact", methods=["POST"])
def submit_contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    
    if name and email and message:
        try:
            msg = Message("New Contact via The Journey Home",
                          sender=email,
                          recipients=["your_email@gmail.com"]) # Replace with your email
            msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            mail.send(msg)
            return redirect(url_for("contact", success="true"))
        except Exception as e:
            print("Email send error:", e)
            return redirect(url_for("contact", error="true"))
    else:
        return redirect(url_for("contact", error="true"))

if __name__ == '__main__':
    app.run(debug=True)