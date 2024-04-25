from flask import Flask
app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Hello World'



@app.route('/shantonu')
def shantonu():
    return 'Hi I am Shantonu Acharjee.'




if __name__ == '__main__':
    app.run(debug=True)
