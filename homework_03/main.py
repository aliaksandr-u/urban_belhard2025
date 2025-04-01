from flask import Flask, render_template
import os

BASE_DIR = os.getcwd()

app = Flask(__name__,
            static_folder=os.path.join(BASE_DIR, 'static'),
            template_folder=os.path.join(BASE_DIR, 'templates'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sheet1/")
def sheet1():
    return render_template("1.html")
    
@app.route('/sheet2/')
def sheet2():
    return render_template("2.html") 

@app.route('/sheet3/')
def sheet3():
    return render_template("3.html")     

@app.errorhandler(404)
def page_not_found(error):
    return '<h1 style="color:red">такой страницы не существует</h1>'

app.run(debug=True)