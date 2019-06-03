

from flask import Flask, render_template, url_for


app = Flask(__name__)

info = "Minimal Flask page"

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html', posts = info)


if __name__ == '__main__':
    app.run(debug=True)