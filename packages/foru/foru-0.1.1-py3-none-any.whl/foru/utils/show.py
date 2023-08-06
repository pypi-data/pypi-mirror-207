import logging

from prettytable import PrettyTable
import xml.etree.ElementTree as ET


def list_songs(songs) -> str:
    pt = PrettyTable(['Index', 'Title', 'Artist', 'Album', 'Duration'])
    for idx, song in enumerate(songs):
        pt.add_row([idx, song.title, song.artist, song.album, show_duration(song.duration)])
    return str(pt)


def list_providers(providers, cur) -> str:
    pt = PrettyTable(['Index', 'Provider'])
    for idx, provider in enumerate(providers):
        print(provider)
        pt.add_row([idx if provider != cur else '*', provider.name])
    return str(pt)


def show_duration(duration):
    if duration is not None:
        seconds = duration
        m, s = divmod(seconds, 60)
    else:
        m, s = 0, 0
    return '{:02}:{:02}'.format(int(m), int(s))


def change_style(app, theme):
    with open('./resource/theme/main.qss', 'r') as f:
        temp = f.read()
    style = repalce_color(temp, theme)
    logging.debug(style)
    app.setStyleSheet(style)


def repalce_color(style_text: str, name: str) -> str:
    try:
        tree = ET.parse(f'./resource/theme/{name}.xml')
        root = tree.getroot()
        colors = {}

        for child in root:
            colors[child.get('name')] = child.text

        style_text = style_text.replace('PRIMARY_COLOR', colors['PRIMARY_COLOR'])
        style_text = style_text.replace('SECONDARY_BACKGROUND_COLOR', colors['SECONDARY_BACKGROUND_COLOR'])
        style_text = style_text.replace('SECONDARY_COLOR', colors['SECONDARY_COLOR'])
        style_text = style_text.replace('PRIMARY_TEXT_COLOR', colors['PRIMARY_TEXT_COLOR'])
        style_text = style_text.replace('SECONDARY_TEXT_COLOR', colors['SECONDARY_TEXT_COLOR'])
        style_text = style_text.replace('BACKGROUND_COLOR', colors['BACKGROUND_COLOR'])
        return style_text
    except Exception as e:
        logging.exception(e)
    return ''
