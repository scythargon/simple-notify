#!/usr/bin/env -S python
import os
import sys
import time
import logging

import psutil
import schedule
from slack_sdk import WebClient


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('simple-notify')

# TODO: add a sane run arguments help and a corresponding library.

if not os.environ.get('DRYRUN'):
    token = os.environ.get('SLACK_BOT_TOKEN')
    if not token:
        print("Please set SLACK_BOT_TOKEN env variable.")
        sys.exit(1)

    slack_channel = os.environ.get('SLACK_CHANNEL')
    if not slack_channel:
        print("Please set SLACK_CHANNEL env variable.")
        sys.exit(1)

space_limit = os.environ.get('SPACE_LIMIT')
if not space_limit:
    print("Please set SPACE_LIMIT env variable (in GB).")
    sys.exit(1)

check_period = os.environ.get('CHECK_PERIOD')
if not check_period:
    print("Please set CHECK_PERIOD env variable.")
    sys.exit(1)

period_units = os.environ.get('PERIOD_UNITS')
if not period_units:
    print("Please set PERIOD_UNITS env variable (seconds/minutes/hours/days).")
    sys.exit(1)

available_values = ["seconds", "minutes", "hours", "days"]
if period_units not in available_values:
    print(f"PERIOD_UNITS should be one of {available_values}.")
    sys.exit(1)

# TODO: Add conversion error handling here.
space_limit = int(space_limit)
check_period = int(check_period)


# print(token, channel, space_limit)

def send_alarm(space_left):
    msg = f'Only {space_left:.2f}GB left!'
    print(msg)
    if not os.environ.get('DRYRUN'):
        slack_client = WebClient(token=token)
        slack_client.chat_postMessage(channel=slack_channel, text=msg)


def check_hdd():
    hdd = psutil.disk_usage('/')
    free_gb = hdd.free / (2**30)
    # print(free_gb)
    if free_gb < space_limit:
        send_alarm(free_gb)
    else:
        logger.info(f'{free_gb:.2f}GB are free so far.')

# Create a schedule.

s = schedule.every(check_period)

if period_units == "seconds":
    s = s.seconds
elif period_units == "minutes":
    s = s.minutes
elif period_units == "hours":
    s = s.hours
elif period_units == "days":
    s = s.days
else:
    print("What a hell?")
    sys.exit(1)

s.do(check_hdd)

# schedule.every(3).seconds.do(check_hdd)


while True:
    schedule.run_pending()
    time.sleep(0.1)
