#!/usr/bin/env python3
'''Creates the template for a new problem'''

import os
import requests
from urllib.parse import urlparse
from argparse import ArgumentParser
from termcolor import colored
from genmd import refresh_markdown


VERIFY = True


def extract_title(url):
    path = urlparse(url).path

    # drop trailing slash
    path = path[:-1] if path[-1] == '/' else path
    return os.path.split(path)[-1]


def file_name(id, title, kind='src'):
    ''' Generates file name from problem id and title '''
    fn_template = 'p{id:0>4d}_{title}.py'
    if kind == 'tst':
        fn_template = 'test_' + fn_template

    return fn_template.format(
        id=id,
        title=title.replace('-', '_')
    )


def verify_url(url):
    if VERIFY:
        try:
            # TODO: verify this url belongs to leetcode domain
            r = requests.get(url, timeout=3)
            if r.status_code != 200:
                raise Exception('bad url')
        except:
            print(colored('Broken link: {link}'.format(
                link=url
            ), 'red'))
            return False
    return True


def verify_path(file_path):
    if VERIFY:
        if os.path.isfile(file_path):
            print(colored('Already exists: {file}'.format(
                file=file_path
            ), 'red'))
            return False
    return True


def src_template(id, title):
    return ''


def tst_template(id, title):
    return (
'''import pytest
from leetcode.{src} import {method}


@pytest.mark.parametrize(('a', 'expectation'), (
    ((), ()),
))
def test_(a, expectation):
    assert {method}(a) == expectation
'''
    ).format(
        src=file_name(id, title, 'src')[:-3], # without .py extension
        method='solve'
    )


def create_files(id, url):
    title = extract_title(url)
    src = os.path.join('leetcode', file_name(id, title, 'src'))
    tst = os.path.join('tests', file_name(id, title, 'tst'))

    valid = verify_url(url)
    valid = verify_path(src) and valid
    valid = verify_path(tst) and valid

    if not valid:
        return False

    with open(src, 'w') as f:
        f.write(src_template(id, title))
        print(colored('Created {}'.format(src), 'green'))

    with open(tst, 'w') as f:
        f.write(tst_template(id, title))
        print(colored('Created {}'.format(tst), 'green'))

    return True


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--skip-verification', action='store_true', help='skip file and url verification')
    parser.add_argument('id')
    parser.add_argument('url')
    args = parser.parse_args()

    VERIFY = not args.skip_verification

    try:
        # we dont want to parse HTML and extract the id
        # from the page, because it goes against
        # the leetcode usage policy
        id = int(args.id)
        url = args.url

        if create_files(id, url):
            refresh_markdown('README.md', False, True)
            print(colored('Updated README.md\n', 'green'))
    except Exception as e:
        print(colored('\nfailed: {}\n'.format(e), 'red'))