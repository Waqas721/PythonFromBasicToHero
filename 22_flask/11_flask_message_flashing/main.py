from flask import Flask,render_template,flash,redirect

app = Flask(__name__)

app.secret_key="dvndvshsvhcvw222v4vndsvndfsjdb434benbej2e2n"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("You have been logged out !","success")
    return render_template("logout.html")

app.run(debug=True)