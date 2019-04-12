#!/usr/bin/env python3
'''Generates markdown table with list of problems'''

import six
import os
import requests
from argparse import ArgumentParser
from pytablewriter import MarkdownTableWriter


VERIFY_LINKS = False

TABLE_TITLE = 'List of Problems'
SRC_FOLDER = './leetcode'
TESTS_FOLDER = 'tests'

LEETCODE_URL = 'https://leetcode.com/problems/{}/'
GITHUB_SRC = 'leetcode/{}'
GITHUB_TST = 'tests/test_{}'
LINK_TEMPLATE = '[{title}]({link})'
GITHUB_URL_TEMPLATE = 'https://github.com/weak-head/leetcode/blob/master/{}'


def verify_url(url):
    if VERIFY_LINKS:
        r = requests.get(url, timeout=1)
        if r.status_code != 200:
            print('Broken link [{status}]: {link}'.format(
                status=r.status_code,
                link=url
            ))


def verify_file(file_path):
    if VERIFY_LINKS:
        if not os.path.isfile(file_path):
            print('Missing file: {path}'.format(
                path=file_path
            ))


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

            # compose leetcode link
            leetcode_url = LEETCODE_URL.format(name.replace('_', '-'))
            leetcode_link = LINK_TEMPLATE.format(
                title=name.replace('_', ' ').title(),
                link=leetcode_url
            )
            verify_url(leetcode_url)

            # compose github src link
            src_url = GITHUB_SRC.format(file)
            src_link = LINK_TEMPLATE.format(
                title='src',
                link=src_url
            )
            verify_url(GITHUB_URL_TEMPLATE.format(src_url))
            verify_file(src_url)

            # compose github tst link
            tst_url = GITHUB_TST.format(file)
            tst_link = LINK_TEMPLATE.format(
                title='tst',
                link=tst_url
            )
            verify_url(GITHUB_URL_TEMPLATE.format(tst_url))
            verify_file(tst_url)

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
    parser = ArgumentParser()
    parser.add_argument('--verify', action='store_true', help='verify links')
    args = parser.parse_args()

    VERIFY_LINKS = args.verify

    refresh_markdown('README.md')