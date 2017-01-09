from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Anand'}
	return render_template('index.html', title='AnandHome', user=user)

@app.route('/inlinehtml')
def inlinehtml():
    user = {'nickname': 'Anand'}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''

@app.route('/withouttitle')
def withouttitle():
	user = {'nickname': 'NoTitle'}
	return render_template('index.html', user=user)

@app.route('/loops')
def loops():
	user = {'nickname': 'loops'}
	posts = [
		{
			'author':{'nickname': 'John'},
			'body': 'Beautiful day in Portland'
		},
		{
			'author':{'nickname': 'Susan'},
			'body': 'The Big Short Movie was awesome!'
		}
	]
	return render_template('index.html', title='AnandHome', user=user,posts=posts)

@app.route('/inherit')
def inherit():
	user = {'nickname': 'loops'}
	posts = [
		{
			'author':{'nickname': 'John'},
			'body': 'Beautiful day in Portland'
		},
		{
			'author':{'nickname': 'Susan'},
			'body': 'The Big Short Movie was awesome!'
		}
	]
	return render_template('inherit.html', title='AnandHome', user=user,posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html', title='Sign In', form=form,
		providers=app.config['OPENID_PROVIDERS'])