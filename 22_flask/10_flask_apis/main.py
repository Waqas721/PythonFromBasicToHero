from flask import Flask,render_template,jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks={
        "Waqas":99,
        "Hamza":88,
        "Ahmed":87,
        "Hitesh":88,
        "Abbas":68,
        "Dinesh":98,
        "Sara":99
    }
    values=[1,marks,67]
    return jsonify(values)

app.run(debug=True)