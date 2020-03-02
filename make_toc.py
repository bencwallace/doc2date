#!/usr/bin/env python3
import json
import re
import sys

def make_toc(file_in, file_out):
    with open(file_in, 'r') as f:
        data = json.loads(f.read())

    cells = data['cells']
    md_cells = filter(lambda c: c['cell_type'] == 'markdown', cells)
    md_sources = map(lambda c: c['source'], md_cells)
    
    pattern = re.compile('(?<!#)##(?!#)')
    headings = []
    for lines in md_sources:
        for line in lines:
            if pattern.match(line):
                headings.append(line.strip('#').strip())

    with open(file_out, 'w') as f:
        f.write('## Contents\n\n')
        for i, heading in enumerate(headings):
            dest = '-'.join(heading.split())
            f.write(f'{i+1}. [{heading}](#{dest})\n')


if __name__ == '__main__':
    files = [(f'doc2date-0{i}.ipynb', f'toc-0{i}.md') for i in range(1, 4)]
    for file_in, file_out in files:
        make_toc(file_in, file_out)
