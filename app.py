"""A simple Flask web application that serves a hello world endpoint."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Return a simple hello world message.

    Returns:
        str: A greeting message.
    """
    return "hello world"
