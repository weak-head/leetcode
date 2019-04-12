#!/usr/bin/env python3

'''Generates markdown table with list of problems'''

import six
import os
import requests
from pytablewriter import MarkdownTableWriter


TABLE_TITLE = 'List of Problems'
SRC_FOLDER = './leetcode'
TESTS_FOLDER = 'tests'
LEETCODE_URL = 'https://leetcode.com/problems/{}/'
GITHUB_SRC = 'leetcode/{}'
GITHUB_TST = 'tests/test_{}'
LINK_TEMPLATE = '[{title}]({link})'


def verify_url(url):
    r = requests.get(url)
    print(r.status_code)
    return r.status_code == 200


def parse_filename(file_name):
    ''' Filename pattern: pXXXX_<url_part>.py '''
    id = file_name[1:5]    # XXXX
    name = file_name[6:-3] # <url_part>
    return id, name


def gen_table():
    header = ['#', 'Title', 'Solution', 'Test cases']
    table = []

    for file in os.listdir(SRC_FOLDER):
        # if problem
        if file[0] == 'p':
            id, name = parse_filename(file)

            # verify leetcode url
            leetcode_url = LEETCODE_URL.format(name.replace('_', '-'))
            if not verify_url(leetcode_url):
                print('Failed for {}'.format(leetcode_url))

            # compose leetcode link
            leetcode_link = LINK_TEMPLATE.format(
                title=name.replace('_', ' ').title(),
                link=leetcode_url
            )

            # compose github src link
            src_url = GITHUB_SRC.format(name)
            src_link = LINK_TEMPLATE.format(
                title='src',
                link=src_url
            )

            # compose github tst link
            tst_url = GITHUB_TST.format(name)
            tst_link = LINK_TEMPLATE.format(
                title='tst',
                link=tst_url
            )

            table.append([id, leetcode_link, src_link, tst_link])

    return header, table


def to_markdown(title, header, table):
    writer = MarkdownTableWriter()

    writer.table_name = title
    writer.headers = header
    writer.value_matrix = table
    writer.margin = 1

    writer.stream = six.StringIO()
    writer.write_table()

    return writer.stream.getvalue()


def refresh_markdown(file_name):
    content = ''
    with open(file_name, 'r') as readme:
        content = readme.read()

    # Drop the old table
    title_loc_ix = content.find(TABLE_TITLE)
    content = content[:title_loc_ix-2] # drop '# '

    # Generate a new one
    header, table = gen_table()
    markdown = to_markdown(TABLE_TITLE, header, table)

    content = content + markdown
    with open(file_name, 'w') as readme:
        readme.write(content)


if __name__ == '__main__':
    refresh_markdown('README.md')