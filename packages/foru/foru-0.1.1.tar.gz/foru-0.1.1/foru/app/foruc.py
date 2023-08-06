#! /usr/bin/env python
import argparse
import sys

import requests

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='foru cli clinet')

    subparsers = parser.add_subparsers(title='subcommands', description='valid commands')
    status_parser = subparsers.add_parser('status')
    status_parser.set_defaults(command='status')

    pause_parser = subparsers.add_parser('pause')
    pause_parser.set_defaults(command='pause')

    stop_parser = subparsers.add_parser('stop')
    stop_parser.set_defaults(command='stop')

    resume_parser = subparsers.add_parser('resume')
    resume_parser.set_defaults(command='resume')

    next_parser = subparsers.add_parser('next')
    next_parser.set_defaults(command='next')

    list_parser = subparsers.add_parser('list')
    list_parser.set_defaults(command='list')

    providers_parser = subparsers.add_parser('providers')
    providers_parser.set_defaults(command='providers')

    select_parser = subparsers.add_parser('select')
    select_parser.add_argument('n', type=int)
    select_parser.set_defaults(command='select')

    previous_parser = subparsers.add_parser('previous')
    previous_parser.set_defaults(command='previous')

    search_parser = subparsers.add_parser('search')
    search_parser.add_argument('kw')
    search_parser.add_argument('-t', '--type', default='song')
    search_parser.set_defaults(command='search')

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('n', type=int)
    add_parser.set_defaults(command='add')

    remove_parser = subparsers.add_parser('remove')
    remove_parser.add_argument('n', type=int)
    remove_parser.set_defaults(command='remove')

    play_parser = subparsers.add_parser('play')
    play_parser.add_argument('n', type=int)
    play_parser.set_defaults(command='play')

    mode_parser = subparsers.add_parser('mode')
    mode_parser.add_argument('n', type=int, choices=[0, 1, 2, 3],
                             help='0 NROMAL, 1 REPEAT_ALL, 2 REPEAT_ONE, 3 SHUFFLE')
    mode_parser.set_defaults(command='mode')

    parser.add_argument('-s', '--server', default='localhost')
    parser.add_argument('-p', '--port', default='9527')

    args = parser.parse_args()

    socket = f'http://{args.server}:{args.port}'
    try:
        server_status = requests.get(socket, timeout=2)
    except TimeoutError or ConnectionRefusedError as e:
        print('Server is not running.')
        sys.exit(1)
    # match args.command:
    if args.command == 'status':
        res = requests.get(f'{socket}/status', timeout=2)
        if res.status_code == 200:
            print(res.text)
        else:
            print('Player error')
    elif args.command == 'pause':
        res = requests.get(f'{socket}/pause', timeout=2)
        if res.status_code != 200:
            print('Player error')
    elif args.command == 'resume':
        res = requests.get(f'{socket}/resume', timeout=2)
        if res.status_code != 200:
            print('Player error')
    elif args.command == 'next':
        res = requests.get(f'{socket}/next', timeout=2)
        if res.status_code != 200:
            print('Player error')
    elif args.command == 'previous':
        res = requests.get(f'{socket}/previous', timeout=2)
        if res.status_code != 200:
            print('Player error')
    elif args.command == 'list':
        res = requests.get(f'{socket}/playinglist', timeout=2)
        if res.status_code == 200:
            print(res.text)
        else:
            print('Player error')
    elif args.command == 'play':
        res = requests.get(f'{socket}/play/{args.n}', timeout=2)
        if res.status_code != 200:
            print('Player error')
    elif args.command == 'add':
        res = requests.get(f'{socket}/add/{args.n}', timeout=2)
        if res.status_code != 200:
            print('Player error')
    elif args.command == 'remove':
        res = requests.get(f'{socket}/remove/{args.n}', timeout=2)
        if res.status_code != 200:
            print('Player error')
    elif args.command == 'search':
        if args.type == 'song':
            res = requests.get(f'{socket}/searchSong/{args.kw}', timeout=2)
            print(res.text)
        else:
            print('Player error')
    elif args.command == 'stop':
        res = requests.get(f'{socket}/stop', timeout=2)
        if res.status_code != 200:
            print('Player error')
    elif args.command == 'providers':
        res = requests.get(f'{socket}/providers', timeout=2)
        if res.status_code != 200:
            print('Player error')
        else:
            print(res.text)
    elif args.command == 'select':
        res = requests.get(f'{socket}/select/{args.n}', timeout=2)
        if res.status_code != 200:
            print('Player error')
    elif args.command == 'mode':
        res = requests.get(f'{socket}/mode/{args.n}', timeout=2)
        if res.status_code != 200:
            print('Player error')
