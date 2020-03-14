from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("index.html")
    else:
        return("Method not allowed",405)
