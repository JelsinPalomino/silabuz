from flask import Flask, render_template

app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def index():
    nombre = "Jelsin Palomino"
    return render_template("index.html", nombre=nombre)


