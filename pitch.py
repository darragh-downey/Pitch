# ZeroMQ demo server

import time
import zmq

context = zmq.Context()
sock = context.socket(zmq.REP)
sock.bind("tcp://*:5555")

while True:
    message = sock.recv()
    print("Recieved request: %s" % message)

    time.sleep(1)

    sock.send(b"World")