import socketio
import json
import time
import random


pos = {
    "position": {
        "x": 2, 
        "y": 1, 
        "z": 3,
        }, 
    "accel": {
        "x": 0.1,
        "y": 0.2,
        "z": 1,
        }
    }

sio = socketio.Client()

def rand_pos():
    r = random.uniform(-1, 1)
    if (r < 0):
        pos["position"]["z"] -= 0.1 
    else:
        pos["position"]["z"] += 0.1
    print(pos)


@sio.event
def connect():
    print('connection established')

@sio.event
def receive_message(data):
    print('message received with ', data)
    #sio.emit('receive_message', {'response': 'my response'})
    

@sio.event
def disconnect():
    print('disconnected from server')

def loop_emit():
    while (True):
        r = random.uniform(-1, 1)
        i=0
        while (i < 10):
            if (r < 0):
                pos["position"]["z"] -= 0.5 
            else:
                pos["position"]["z"] += 0.5
            pos_json = json.dumps(pos)
            sio.emit('locator-to-server', pos_json)
            #rand_pos()
            time.sleep(0.1)
            i += 1

        #sio.wait()

def main():
    sio.connect('http://localhost:3001')
    loop_emit()
    

if __name__ == '__main__':
    main()