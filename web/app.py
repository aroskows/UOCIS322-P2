"""
Alexa Roskowski's Flask API.
"""

from flask import Flask, abort, render_template
import os

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html')

@app.route("/<path:name>")
def logic(name):
    if "~" in name or "//" in name or ".." in name:
        #break --> give a 403 error code
        abort(403)
    elif name[-5:] == '.html' or name[-4:] == '.css':
        if name in os.listdir(os.curdir):
            f = open(name, "r") 
            return f.read()
        else:
            abort(404)
    else: 
        return "UOCIS docker demo! \n"

@app.route("/")
def hello():
     return "UOCIS docker demo! \n"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
