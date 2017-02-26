#!/usr/bin/python
#coding:utf-8

import sys
import re
import time
import datetime
import socket
try:
    import simplejson as json
except:
    import json

import subprocess
from raven import Client

import requests

last_sent = 0

dsn = '__SENTRY_DSN__'

#00 - '19:07:03'
#01 - '9663'
#02 - 'be/4'
#03 - 'nginx'
#04 - '10423.06'
#05 - 'K/s'
#06 - '10423.06'
#07 - 'K/s'
#08 - '0.00'
#09 - '%'
#10 - '99.99'
#11 - '%'
#12 - 'php-fpm: pool www'

def should_skip(program):
    if program == '[kjournald]':
        return True

    for prefix in ['gzip', 'rsync', 'ssh', 'logrotate', 'sap100', 'sar ', 'rpm ', 'updatedb', 'mysql', 'nginx', 'vim', 'cat']:
        if program.startswith(prefix):
            return True

    return False

def run_command(*cmd):
    try:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if err:
            raise Exception(err.strip())
        return out
    except Exception, e:
        return 'run %s failed: %s' % (str(cmd), e)

while True:
    try:
        line = sys.stdin.readline().strip()
    except KeyboardInterrupt:
        print >>sys.stderr, "user abort"
        sys.exit(0)

    fields = re.split(' +', line.strip(), 12)
    if len(fields) != 13:
        continue

    if should_skip(fields[12]):
        continue

    read_speed  = float(fields[4])
    write_speed = float(fields[6])
    if read_speed > 1000 or write_speed > 1000:
        date = time.strftime('%Y-%m-%d')
        pid = fields[1]
        client = Client(dsn)
        message = '%s: PID(%s) IS USING TOO MUCH DISK IO' % (socket.gethostname(), pid)
        args = {
            'time'  : date + ' ' + fields[0],
            'iotop' : line.strip(),
            'proc'  : run_command('ls', '-lhR', '/proc/%s/fd' % pid),
        }
        print >>sys.stderr, message
        print >>sys.stderr, json.dumps(args, indent=4)
        client.capture('raven.events.Message', message=message, extra=args)

# https://www.felix021.com/blog/read.php?2170