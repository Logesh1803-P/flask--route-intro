from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

@app.route("/hi/<name>")
def hello(name):
    return "hello{}".format(name)

@app.route("/welcome/<name>")
def welcome(name):
    return render_template('index.html',perro=name)   

if __name__ == "__main__":
    app.run(debug=True)



    # C:\Users\admin\AppData\Local\Programs\Python\Python310