"""A simple Flask web application that serves a hello world endpoint."""

from flask import Flask
from flaskr.hello_world_fn import hello_world_fn

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Return a hello world message when accessing the root endpoint.

    Returns:
        str: A hello world message
    """
    message = hello_world_fn()
    return message


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
