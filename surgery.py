#!/usr/bin/env python

import os
import sys
import tornado

ioloop_file = os.path.dirname(tornado.__file__) + '/ioloop.py'
f = open(ioloop_file, 'w')
f.write('from zmq.eventloop.ioloop import *')
f.close()
