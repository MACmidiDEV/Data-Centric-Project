from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("app.html")

@app.route("/about")
def landing():
    return render_template("landingPage.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


      
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)

            