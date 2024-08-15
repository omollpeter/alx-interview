#!/usr/bin/python3

import sys, random, re
from datetime import datetime

# for line in sys.stdin:
#     sys.stdout.write(line)

# print(datetime.now())

# print(random.choice([100,200,300]))

input_format = r'^(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "([^"]*)" \d{3} \d+$'

entry = '89.163.118.142 - [2024-08-15 10:52:25.093388] "GET /projects/260 HTTP/1.1" 500 251'

match = re.match(input_format, entry)

if match:
    print("Valid")
else:
    print("Not valid")
