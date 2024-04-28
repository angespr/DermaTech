from flask import Flask, render_template, request, url_for, session, redirect

from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required

from flask_bcrypt import Bcrypt

from gpt import gpt_response_extracter

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        # store the password or whatever
        username = request.form.get("username")
        password = request.form.get("password")

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template("signup.html")
        
        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("about.html"))
        
    else:

        return render_template("signup.html")
    

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for("about.html"))
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route("/survey", methods=['POST', 'GET'])
@login_required
def survey():
    pass
    

#print(gpt_response_extracter("Fuck"))



if __name__ == "__main__":
    with app.app_context():   
        db.create_all()
    app.run(debug=True)
 