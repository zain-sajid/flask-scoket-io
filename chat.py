from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

if __name__ == '__main__':
    socketio.run(app)


@app.get('/')
def index():
    return "API working!"


@socketio.on('message')
def handle_message(data):
    print(data)
    emit("chat", data, broadcast=True)
