import json

if __name__ == '__main__':
    with open('doc2date.ipynb', 'r') as f:
        data = json.loads(f.read())

    cells = data['cells']
    md_cells = filter(lambda c: c['cell_type'] == 'markdown', cells)
    md_sources = map(lambda c: c['source'], md_cells)
    
    headings = []
    for lines in md_sources:
        for line in lines:
            if line.startswith('##'):
                headings.append(line.strip('#').strip())

    with open('toc.md', 'w') as f:
        f.write('## Contents\n\n')
        for i, heading in enumerate(headings):
            dest = '-'.join(heading.split())
            f.write(f'{i+1}. [{heading}](#{dest})\n')
