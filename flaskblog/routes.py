from flask import render_template, url_for,flash,redirect
from flaskblog import app, db, bcrypt

from flaskblog.forms import RegsitrationForm, LoginForm

from flaskblog.models import User, Post

posts = [
    {
        'author':'Anmol Shukla',
        'title': 'Blog post 1',
        'content':'First post',
        'date_posted':'2nd Nov,2024'
       
    },
    {
         'author':'Biman Kaka',
         'title': 'Blog post 1',
         'content':'First post',
         'date_posted':'2nd Nov,2024'
    }
]





@app.route("/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='about')

@app.route("/register", methods=['GET','POST'])
def register():
   form = RegsitrationForm()
   if form.validate_on_submit():
       hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
       user1 = User(username=form.username.data,email=form.email.data,password=hashed_password)
       db.session.add(user1)
       db.session.commit()
       flash('Account has been created! You can log in!','success')
       return redirect(url_for('login'))
   return render_template('register.html',title='Register', form=form)

@app.route("/login",methods=['GET','POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
       if form.email.data == 'admin@blog.com' and form.password.data == 'password':
           flash('Login Success!','success')
           return redirect(url_for('home'))
       else:
           flash("Login Unsuccessful! Please Check Username and Password!",'danger')
   return render_template('login.html',title='Login', form=form)

