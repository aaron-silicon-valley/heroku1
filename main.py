
from flask import Flask, redirect
from time import sleep

app = Flask(__name__)

@app.route("/")
def navigate():
    sleep(1)
    return redirect("/home")

@app.route("/home")
def home():
    return "flask running"

@app.route("/resume")
def resume():
    return redirect("https://aaron-portfolio.notion.site/Resume-ea4d47dc2f68414f8e7434b13a8e06dd")

if __name__ == "__main__":
    app.run()