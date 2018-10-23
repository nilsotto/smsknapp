#! /usr/bin/python

import requests

xml_string="<sms><til>+4790011048</til><melding>dette er en python-test</melding></sms>"
url="https://varsling-tjenester-felles-develop.cluster.dev/varsle/sms"

requests.post(url, data=xml_string, headers={'Content-Type':'application/xml; charset=UTF-8'},verify=False)
