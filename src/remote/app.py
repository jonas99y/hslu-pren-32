from typing import Dict
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from config.device_config import driver, switch, liftDriver, ledDriver, lift
from hal.led_driver import  Piktogram
from pathlib import Path
import time
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
            ledDriver.ledSet(Piktogram.hammer)
            time.sleep(0.4)
            ledDriver.ledSet(Piktogram.taco)
            time.sleep(0.4)
            ledDriver.ledSet(Piktogram.ruler)
            time.sleep(0.4)
            ledDriver.ledSet(Piktogram.bucket)
            time.sleep(0.4)
            ledDriver.ledSet(Piktogram.pencile)
            time.sleep(0.4)
            ledDriver.ledSet(Piktogram.none)
        elif direction == 5:
            lift.climb()
        elif direction == 6:
            lift.retract()
        else:
            driver.drive(direction)

@socketio.on('speed')
def handle_speed_change(speed):
    print(speed)
    liftDriver.changeSpeed(speed)
    driver.changeSpeed(speed)

if __name__ == '__main__':
    socketio.run(app, port=8988, host='0.0.0.0', ssl_context=(str(Path(__file__).parent/'cert.pem'), str(Path(__file__).parent/'key.pem')))