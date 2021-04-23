from typing import Dict
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from config.device_config import driver, switch, liftDriver
from hal.led_driver import LedDriver, Piktogram

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# switch.init()
@socketio.on('drive')
def handle_drive_instruction(data:Dict):
    print('Drive')
    print(data)
    if 'direction' in data.keys():
        direction:int = data['direction']
        if direction == 0:
            driver.stop()
            liftDriver.stop()
            #test led_driver
            LedDriver.ledSet(Piktogram.hammer)
            LedDriver.ledSet(Piktogram.taco)
            LedDriver.ledSet(Piktogram.bucket)
            LedDriver.ledSet(Piktogram.pencile)
            LedDriver.ledSet(Piktogram.ruler)
            LedDriver.ledSet(Piktogram.none)
        else:
            driver.drive(direction)
            liftDriver.drive(direction)

@socketio.on('speed')
def handle_speed_change(speed):
    print(speed)
    liftDriver.changeSpeed(speed)
    driver.changeSpeed(speed)

if __name__ == '__main__':
    socketio.run(app, port=8988)