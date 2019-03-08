#!/usr/bin/python3
import telethon.sync
import telethon.sessions
import sys
import os
import time


api_id = 71263
api_hash = "8466add9244ac4ba8e9524738add8ce7"


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
                client.send_message(peer, data)
                return client


if __name__=='__main__':
    main()
