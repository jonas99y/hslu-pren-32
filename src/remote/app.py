from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('drive')
def handle_drive_instruction(data):
    print('Drive')
    print(data)

if __name__ == '__main__':
    socketio.run(app, port=8988)