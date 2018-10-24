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
phone_number="+4790011048"
url="https://varsling-tjenester-felles-develop.cluster.dev/varsle/sms"
smses=[ "Nå tenker noen i Husbanken på deg", 
        "Lurer du på om deploy 2.0 er i prod?",
        "3d-printeren ser litt trist ut i dag - den savner nok deg",
        "ping - http://husbanken.no",
        "Mjøndalen - Kjempers hjemsted",
        "Da ses vi bare på JULA i Mjøndalen framover … :( (Hilde)",
        "A small step for you Jan-Stian, a giant leap for Husbanken without you! (Erik E)",
        "Daus! Hva laver du? (Frode S)",
        "Nå skinner sola i Solbergelva – den kommer sikkert snart deg i Mjøndalen også (Antonia)",
        "Nå spilles det ATM, hvor er du (Katrine)",
        "Husbanken will never be the same (Trond V)",
        "Jan-Stian Gabrielli. Gabrielli etter det hebraiske Gever som betyr strong man, hero or God. Sjelden har et etternavn kledd mannen bedre. (Trond V)"] 

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
            number=(delta.seconds % len(smses))
            print("SENDER SMS!!!! %d" % number)
            print(datetime.datetime.now())
            print(smses[number])
            lastTime = datetime.datetime.now()
            xml_string="<sms><til>%s</til><melding>%s</melding></sms>" % (phone_number,smses[number])
            requests.post(url, data=xml_string, headers={'Content-Type':'application/xml; charset=UTF-8'},verify=False)

    event = in_file.read(EVENT_SIZE)

in_file.close()

