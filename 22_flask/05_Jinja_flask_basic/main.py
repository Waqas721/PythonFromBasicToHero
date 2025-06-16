from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks={
        "Waqas":99,
        "Hamza":88,
        "Ahmed":87,
        "Hitesh":88,
        "Abbas":68,
        "Dinesh":98
    }
    return render_template("index.html",marks=marks)

app.run(debug=True)