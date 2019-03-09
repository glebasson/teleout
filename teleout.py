#!/usr/bin/python3
import config
import re
import telethon.sync
import telethon.sessions
import sys
import os
import time


api_id = config.api_id
api_hash = config.api_hash


def splitData(data):
    # split data into messages
    messages = []
    while len(data) > 2048:
        messages.append(data[:4096])
        data = data[4096:]
    if data:
        messages.append(data)
    return messages


def main():
    # storage data from pipe
    data = sys.stdin.read()

    filepath = os.path.expanduser('~/.config/teleout.session')
    if not os.path.isfile(filepath):
        # reboot interactive session for terminal
        sys.stdin = open(os.ttyname(1), 'r')
        # Get client and save string for future connections
        with telethon.sync.TelegramClient(telethon.sessions.StringSession(), api_id, api_hash) as client:
            s = client.session.save()
            with open(filepath, 'w+') as f:
                f.write(s)
                f.close()

    else:
        d = os.path.expanduser('~/.config/teleout.session')
        with open(d, 'r') as f:
            s = f.read()
            with telethon.sync.TelegramClient(telethon.sessions.StringSession(s), api_id, api_hash) as client:
                try:
                    peer = int(sys.argv[1])
                except:
                    peer = sys.argv[1]
                messages = splitData(data)
                iLast = len(messages) - 1
                for index, message in enumerate(messages):
                    client.send_message(peer, message)
                    if index != iLast:
                        time.sleep(1)
                return client


if __name__=='__main__':
    main()
