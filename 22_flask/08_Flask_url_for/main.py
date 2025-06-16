from flask import Flask,render_template

#app = Flask(__name__,static_url_path="/public") # this is how you change static url path
app = Flask(__name__,static_folder="assets",static_url_path="/public") # chnaging static folder location
@app.route("/")
def home():
    return render_template("index.html")

app.run(debug=True)