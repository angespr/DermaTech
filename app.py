from flask import Flask, render_template, request, url_for, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        # store the password or whatever
        username = request.form.get("username")
        password = request.form.get("password")
        return render_template("about.html")
    else:
        return render_template("signup.html")
    
    
@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        return render_template("about.html")
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
 