

from flask import Flask, render_template, url_for


app = Flask(__name__)

# a variable containing place holder newlines
blog_posts = str(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html', posts = blog_posts)

@app.route('/about')
def aboutpage():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug=True)