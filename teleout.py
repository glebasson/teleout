#!/usr/bin/python3
import telethon.sync
import telethon.sessions
import sys
import os
import time


api_id = 17349
api_hash = "344583e45741c457fe1862106095a5eb"


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

    d = os.path.expanduser('~/.config/teleout.session')
    with open(d, 'r') as f:
        s = f.read()
        with telethon.sync.TelegramClient(telethon.sessions.StringSession(s), api_id, api_hash) as client:
            try:
                peer = int(sys.argv[1])
            except:
                peer = sys.argv[1]
            # split data into messages
            messages = [data[4096*i:4096*(i+1)] for i in range(len(data)//4096+1) if data[4096*i:4096*(i+1)]]
            iLast = len(messages) - 1
            for index, message in enumerate(messages):
                client.send_message(peer, message)
                if index != iLast:
                    time.sleep(1)
            return client


if __name__=='__main__':
    main()
