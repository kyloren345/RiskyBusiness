from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/bibliography')
def bibliography():
    return render_template("bibliography.html")

if __name__ == '__main__':
    app.run(debug=True)