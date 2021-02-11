from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
@app.route('/index')
def index():
  user = {'username': 'tomek'}
  return render_template('/index.html', title = 'micro', user = user['username'] )
 
 
@app.route('/login', methods =['GET', 'POST'])
def login():   
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('index.html')
    return render_template('login.html', title='Sign In', form=form)