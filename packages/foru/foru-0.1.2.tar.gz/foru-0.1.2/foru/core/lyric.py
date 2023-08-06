import re
from typing import Dict


def parse_lyric(content: str) -> Dict[int, str]:
    lyric_map = dict()
    pattern = re.compile(r'\[(\d+):(\d+)\.(\d+)](.*?)$')
    lines = content.splitlines()
    for line in lines:
        m = pattern.search(line, 0)
        if m:
            minu, sec, mil, sent = m.groups()
            lyric_map[int(minu) * 60 * 1000 + int(sec) * 1000 + int(mil)] = sent
    return lyric_map
