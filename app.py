from flask import Flask, render_template,request
from tool import lowerDup
import json

app = Flask(__name__, static_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/duplicate",methods=['POST'])
def dup():
    text = request.form.get("text")
    length = int(request.form.get("length"))
    lower_text,flag = lowerDup(text,length)
    data = {
        "text":lower_text,
        "code": "200" if flag else "404"
    }
    return json.dumps(data)
if __name__ == "__main__":
    app.run()
    