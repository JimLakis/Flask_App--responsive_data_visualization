

from flask import Flask, render_template, url_for

from bokeh.plotting import figure
from bokeh.embed import json_item

import json


app = Flask(__name__)


@app.route('/plot')
def plot():
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]
    p = figure(title="Simple Line Chart", x_axis_label='x-axis', y_axis_label='y-axis', sizing_mode='scale_both')
    p.line(x, y, legend="data set 1", line_width=2)
    return json.dumps(json_item(p, "myplot"))


@app.route('/')
@app.route('/home')
@app.route('/about')
@app.route('/login')
@app.route('/register')
def homepage():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)