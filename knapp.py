#!/usr/bin/python
# coding=utf-8

import struct
import time
import sys
import datetime
import requests

infile_path = "/dev/input/event" + (sys.argv[1] if len(sys.argv) > 1 else "0")

#long int, long int, unsigned short, unsigned short, unsigned int
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)
#xml_string="<sms><til>+4790011048</til><melding>dette er en python-test</melding></sms>"
#url="https://varsling-tjenester-felles-develop.cluster.dev/varsle/sms"
#smses=[ "Nå tenker noen i Husbanken på deg", "Lurer du på om deploy 2.0 er i prod?", "3d-printeren ser trist ut i dag", "ping - http://husbanken.no", "Mjøndalen - Kjempers hjemsted", "" ] 

#open file in binary mode
in_file = open(infile_path, "rb")

event = in_file.read(EVENT_SIZE)

lastTime = datetime.datetime.now()

while event:
    (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)

    if type != 0 or code != 0 or value != 0:
        now = datetime.datetime.now()
        delta = now - lastTime
        if (code == 4 and delta.seconds > 3):
            number=delta.seconds % 8
            print("SENDER SMS!!!!" + number
            lastTime = datetime.datetime.now()
            #requests.post(url, data=xml_string, headers={'Content-Type':'application/xml; charset=UTF-8'},verify=False)

    event = in_file.read(EVENT_SIZE)

in_file.close()

