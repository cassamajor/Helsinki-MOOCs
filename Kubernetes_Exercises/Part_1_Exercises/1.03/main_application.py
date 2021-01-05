#!/usr/bin/env python3

""" https://devopswithkubernetes.com/part-1/1-first-deploy Exercise 1.01 """

import datetime
import secrets
import time

while True:
    try:
        print(f'{datetime.datetime.utcnow()}: {secrets.token_urlsafe()}', flush=True)
        time.sleep(5)
    except KeyboardInterrupt:
        print()
        exit()
