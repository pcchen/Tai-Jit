#!/usr/bin/env python3
"""Convert ruby notation from 漢字[かな] to {漢字(かな)} in markdown files."""

import re
import sys
import glob

# Match CJK characters followed by [reading]
# CJK Unified Ideographs: U+4E00-U+9FFF, U+3400-U+4DBF, U+F900-U+FAFF
PATTERN = re.compile(
    r'([\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]+)\[([^\[\]]+)\]'
)


CIRCLED_IDEOGRAPHS = '㊀㊁㊂㊃㊄㊅㊆㊇㊈㊉'  # 1-10
PAREN_NUMBER = re.compile(r'[(\uff08](\d{1,2})[)\uff09]')


def convert_paren_number(match):
    n = int(match.group(1))
    if 1 <= n <= 10:
        return CIRCLED_IDEOGRAPHS[n - 1]
    return match.group(0)


def convert_line(line):
    line = PAREN_NUMBER.sub(convert_paren_number, line)
    return PATTERN.sub(r'{\1(\2)}', line)


def convert_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()

    converted = '\n'.join(convert_line(line) for line in original.split('\n'))

    if converted != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(converted)
        print(f'converted: {path}')
    else:
        print(f'no change: {path}')


def main():
    paths = sys.argv[1:] if len(sys.argv) > 1 else glob.glob('docs/*.md')
    for path in paths:
        convert_file(path)


if __name__ == '__main__':
    main()
