#!/usr/bin/python

from urllib.request import urlopen
CUSTOMER_DATAFILE = 'https://raw.githubusercontent.com/jiminny/join-the-team/master/assets/customer-channel.txt'
USER_DATAFILE = 'https://raw.githubusercontent.com/jiminny/join-the-team/master/assets/user-channel.txt'

def parse_datafile(target_url):
    call_data = ''
    for line in urlopen(target_url):
        call_data += line.decode("utf-8")
        print(line)

    return call_data


def init():
    print(parse_datafile(CUSTOMER_DATAFILE))



init()
