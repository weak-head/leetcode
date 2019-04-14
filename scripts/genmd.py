#!/usr/bin/env python3
'''Generates markdown table with list of problems'''

import six
import os
import requests
from argparse import ArgumentParser
from pytablewriter import MarkdownTableWriter
from termcolor import colored


TABLE_TITLE = 'List of Problems'

LEETCODE_URL = 'https://leetcode.com/problems/{}/'
GITHUB_URL = 'https://github.com/weak-head/leetcode/blob/master/{}'
GITHUB_SRC = 'leetcode/{}'
GITHUB_TST = 'tests/test_{}'
MD_LINK = '[{title}]({link})'


def verify_url(url, verify=True):
    if verify:
        try:
            r = requests.get(url, timeout=3)
            if r.status_code != 200:
                raise Exception('broken link')
        except:
            print(colored('  Broken link [{status}]: {link}'.format(
                status=r.status_code,
                link=url
            ), 'red'))
            return False
    return True


def verify_file(file_path, verify=True):
    if verify:
        if not os.path.isfile(file_path):
            print(colored('  Missing file: {path}'.format(
                path=file_path
            ), 'yellow'))
            return False
    return True


def next_problem(id, title, silent=False):
    if not silent:
        print('\n{id} - {title}:'.format(
            id=id,
            title=title
        ))


def verification_status(id, title, success, silent=False):
    if success and not silent:
        print(colored('  OK', 'green'))


def parse_filename(file_name):
    ''' Filename pattern: pXXXX_<url_part>.py '''
    id = file_name[1:5]    # XXXX
    name = file_name[6:-3] # <url_part>
    return id, name


def gen_table(verify=False, silent=False):
    header = ['#', 'Title', 'Solution', 'Test cases']
    table = []

    for file in os.listdir('./leetcode'):
        # if problem
        if file[0] == 'p':
            id, name = parse_filename(file)
            problem_title = name.replace('_', ' ').title()
            next_problem(id, problem_title, silent)

            # compose leetcode link
            leetcode_url = LEETCODE_URL.format(name.replace('_', '-'))
            leetcode_link = MD_LINK.format(
                title=problem_title,
                link=leetcode_url
            )
            success = verify_url(leetcode_url, verify)

            # compose github src link
            src_url = GITHUB_SRC.format(file)
            src_link = MD_LINK.format(
                title='src',
                link=src_url
            )
            success = verify_url(GITHUB_URL.format(src_url), verify) and success
            success = verify_file(src_url, verify) and success

            # compose github tst link
            tst_url = GITHUB_TST.format(file)
            tst_link = MD_LINK.format(
                title='tst',
                link=tst_url
            )
            success = verify_url(GITHUB_URL.format(tst_url), verify) and success
            success = verify_file(tst_url, verify) and success

            verification_status(id, name, success, silent)
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


def refresh_markdown(file_name, verify=False, silent=False):
    content = ''
    with open(file_name, 'r') as readme:
        content = readme.read()

    # Drop the old table
    title_loc_ix = content.find(TABLE_TITLE)
    content = content[:title_loc_ix-2] # drop '# '

    # Generate a new one
    header, table = gen_table(verify, silent)
    markdown = to_markdown(TABLE_TITLE, header, table)

    content = content + markdown
    with open(file_name, 'w') as readme:
        readme.write(content)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--verify', action='store_true', help='verify links')
    args = parser.parse_args()

    try:
        refresh_markdown('README.md', args.verify, False)
        print()
    except:
        print('\nterminated\n')