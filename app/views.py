from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user={"name":"karthik"}
    posts=[{"author":{"name":"harsha"},"body":"killer"},{"author":{"name":"pavan"},"body":"victim"}]
    return render_template("index.html",title='Home',user=user,posts=posts)
