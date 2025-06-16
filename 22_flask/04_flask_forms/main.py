from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello_world():
    if(request.method=="POST"):
       # handle the form 
       with open("file.txt","w") as f:
           f.write(f"Name: {request.form['name']} \nEmail: {request.form['email']}")
       return render_template("contact.html")
    else:
        return render_template("contact.html")
        
    

app.run(debug=True)