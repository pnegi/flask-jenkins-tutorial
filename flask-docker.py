from flask import Flask
app = Flask(__name__)

@app.route('/name')
def hello_world():
    return 'Preeti Negi and Chandra Bhanu Rastogi'

@app.route('/')
def hello_worldd():
    return 'root path'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
