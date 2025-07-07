from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from a Python Flask app in Docker!'

if __name__ == '__main__':
    # Note: For production, use a WSGI server like Gunicorn or uWSGI
    # The Dockerfile CMD will typically use a WSGI server.
    app.run(debug=True, host='0.0.0.0', port=5000)
