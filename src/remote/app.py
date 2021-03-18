from typing import Dict
from flask import Flask, render_template
from flask_socketio import SocketIO
from config.device_config import driver, switch

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

switch.init()
@socketio.on('drive')
def handle_drive_instruction(data:Dict):
    # print('Drive')
    # print(data)
    # if 'direction' in data.keys():
    #     direction:int = data['direction']
    #     if direction == 0:
    #         driver.stop()
    #     else:
    #         driver.drive(direction)

    # driver.drive()

if __name__ == '__main__':
    socketio.run(app, port=8988)