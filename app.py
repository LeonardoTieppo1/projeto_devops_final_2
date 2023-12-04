from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def hello():
    return jsonify({'message': 'Hello World and Ola Mundo!'})

if __name__ == '__main__':
    app.run()
