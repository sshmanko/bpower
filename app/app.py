from flask import Flask
app = Flask(__name__)


@app.route('/')
def root_get():
    return 'Success'


@app.route('/ping')
def ping_get():
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
