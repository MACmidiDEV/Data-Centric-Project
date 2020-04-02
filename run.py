from flask import Flask, render_template, request, flash
import json
import os



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
          if request.method == "POST":
            flash("Thanks {}, we have received your message".format(
            request.form["name"]
        ))
    return render_template("app.html")

@app.route("/learn")
def learn():
    data = []
    with open("three/z/data/letters.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("learn.html", page_title="Learn", letters=data)
    
@app.route("/learn/<letter_letter>")
def learn_letter(letter_letter):
    letter = {}
    with open("three/z/data/letters.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == letter_letter:
                letter = obj
    return render_template("letter.html", letter=letter)





      
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)

            