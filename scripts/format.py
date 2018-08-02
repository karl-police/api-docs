import re
import sys

tag_re = re.compile('{% ([\w-]+).* %}')
leading_space_re = '^[\s]{2}'
spaces = 2

def strip_leading_space(line, max = 100):
    r = re.compile('^[\s]{,' + str(max * spaces) + '}')
    return r.sub('', line)

def process(text):
    level = -1
    out = []

    for line in text.splitlines():
        match = tag_re.search(line)
        if match is None:
            line = (level + 1) * spaces * ' ' + strip_leading_space(line, level + 1)
            if re.match('^\s+$', line):
                line = ''
            out.append(line)
            continue

        line = strip_leading_space(line)

        if not match.group(1).startswith('end'):
            level += 1

        space = level * spaces * ' '
        line = space + line

        out.append(line)

        if match.group(1).startswith('end'):
            level -= 1

    # final newline
    if out[-1] != '':
        out.append('')

    return '\n'.join(out)

def format_file(path):
    with open(path, 'r+') as f:
        text = f.read()
        out = process(text)
        if out is not None:
            f.seek(0)
            f.truncate()
            f.write(out)

for path in sys.argv:
    format_file(path)
