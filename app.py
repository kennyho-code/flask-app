"""A simple Flask web application that serves a hello world endpoint."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Return a simple hello world message.

    Returns:
        str: A greeting message.
    """
    return render_template('index.html', message="Hello, World!")


if __name__ == '__main__':
    app.run(debug=True)
