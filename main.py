#!/usr/bin/python

import re
import json
from urllib.request import urlopen, Request

CUSTOMER_DATAFILE = 'https://raw.githubusercontent.com/jiminny/join-the-team/master/assets/customer-channel.txt'
USER_DATAFILE = 'https://raw.githubusercontent.com/jiminny/join-the-team/master/assets/user-channel.txt'

JSON_TEMPLATE = {
    "longest_user_monologue": 0,
    "longest_customer_monologue": 0,
    "user_talk_percentage": 0,
    "user": [

    ],
    "customer": [

    ]
}


def get_channel_data(target_url):
    call_data = []
    lines_num = 0
    max_monologue = 0
    total_talk_time = 0
    duration = 0
    request = Request(target_url)
    total_lines = len(urlopen(request).readlines())
    print("lines are:" + str(total_lines))
    call_input_regex = re.compile(r'silence_(start|end):\s+(\d+\.{0,1}\d+)')
    for line in urlopen(target_url):
        # first line - init call
        if lines_num == 0:
            talk_start = 0

        line_contents = line.decode("utf-8")
        # talk begins
        if line_contents.__contains__("silence_start"):
            # print("boo")
            talk_end = float(re.search(r'silence_start:\s+(\d+\.{0,1}\d+)', line_contents).group(1))
        # talk ends
        elif line_contents.__contains__("silence_end"):
            # print("m00")
            talk_start = float(re.search(r'silence_end:\s+(\d+\.{0,1}\d+)', line_contents).group(1))
        # unreadable line
        else:
            continue

        if lines_num % 2 == 0:
            call_data.insert(int(lines_num / 2), [talk_start, talk_end])
            monologue_duration = talk_end - talk_start
            total_talk_time = total_talk_time + monologue_duration
            if (monologue_duration) > max_monologue:
                max_monologue = round(monologue_duration,2)
        # call_data = call_data.insert(lines_num, line_contents)
        lines_num = lines_num + 1
        # print(lines_num)

        # last line - save duration
        if lines_num == total_lines:
            duration = float(re.search(r'silence_end:\s+(\d+\.{0,1}\d+)', line_contents).group(1))

    return {
        "last_line": lines_num,
        "max_monologue": max_monologue,
        "total_talk_time" : total_talk_time,
        "talks": call_data,
        "duration": duration,
    }


def get_channel_talk_percentage(total_talk_time, call_duration):
     return round(total_talk_time*100/call_duration,2)

def get_talk_duration(customer_data, user_data):
    return max(customer_data["duration"], user_data["duration"])

def populated_json(longest_user_monologue, longest_customer_monologue, user_talk_percentage, user, customer):
    JSON_TEMPLATE["longest_user_monologue"] = longest_user_monologue
    JSON_TEMPLATE["longest_customer_monologue"] = longest_customer_monologue
    JSON_TEMPLATE["user_talk_percentage"] = user_talk_percentage
    JSON_TEMPLATE["user"] = user
    JSON_TEMPLATE["customer"] = customer
    json_string = json.dumps(JSON_TEMPLATE)
    print(json_string)

def init():
    user_data = get_channel_data(CUSTOMER_DATAFILE)
    longest_user_monologue = user_data["max_monologue"]
    #print(user_data)
    customer_data = get_channel_data(USER_DATAFILE)
    longest_customer_monologue = customer_data["max_monologue"]

    #print(customer_data)
    call_duration = (get_talk_duration(user_data, customer_data))
    user_talk_percentage = get_channel_talk_percentage(user_data["total_talk_time"], call_duration)
    return populated_json(longest_user_monologue, longest_customer_monologue, user_talk_percentage, user_data["talks"], customer_data["talks"])


init()
