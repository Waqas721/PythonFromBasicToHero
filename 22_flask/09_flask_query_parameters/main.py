from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    name="Waqas"
    token=444
    if "name" in request.args.keys():
        name=request.args['name']
    if "name" in request.args.keys():
        token=request.args['token']
    return render_template("index.html",name=name,token=token)

app.run(debug=True)