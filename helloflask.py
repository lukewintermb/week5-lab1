from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return """
    <h1>Hello World!<h1>
    <p>I don't know what acronymns are<p>
    <p>But that won't hold me back!<p>
    """

@app.route('/luke')
def wc():
   return render_template("template.html")


@app.route("/task4")
def t_test():
    return render_template("bootstrap_template.html")
