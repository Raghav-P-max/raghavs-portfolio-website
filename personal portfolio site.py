from flask import Flask, render_template, redirect, url_for

app=Flask(__name__)

@app.route("/<name>")
def user(name):
    return f"<h1>Hello there! you have entered /{name} at the end of url. Kindly enter only /about or /index at the end if you want to know more about me!</h1>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route("/redirect")
def go_redirect():
    return redirect(url_for("user", name="Raghav"))

if __name__=="__main__":
    app.run(debug=True)
