#!/usr/bin/env python3
'''Creates a template for the new problem'''

import os
import requests
from argparse import ArgumentParser
from termcolor import colored


VERIFY = True


LEETCODE_URL = 'https://leetcode.com/problems/{}/'
SRC = 'leetcode/{}'
TST = 'tests/{}'


def file_name(id, title, kind='src'):
    ''' Generates file name from problem id and title '''
    fn_template = 'p{id:0>4d}_{title}.py'
    if kind == 'tst':
        fn_template = 'test_' + fn_template

    return fn_template.format(
        id=id,
        title=title.replace('-', '_')
    )


def verify_url(id, title):
    if VERIFY:
        url = LEETCODE_URL.format(title)
        try:
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
        src=file_name(id, title, 'src')[:-3], # no .py extension
        method='solve'
    )


def create_files(id, title):
    src = SRC.format(file_name(id, title, 'src'))
    tst = TST.format(file_name(id, title, 'tst'))

    valid = verify_url(id, title)
    valid = verify_path(src) and valid
    valid = verify_path(tst) and valid

    if not valid:
        return

    with open(src, 'w') as f:
        f.write(src_template(id, title))
        print(colored('Created {}'.format(src), 'green'))

    with open(tst, 'w') as f:
        f.write(tst_template(id, title))
        print(colored('Created {}'.format(tst), 'green'))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--skip-verification', action='store_true', help='skip file and url verification')
    parser.add_argument('id')
    parser.add_argument('title')
    args = parser.parse_args()

    VERIFY = not args.skip_verification

    try:
        id = int(args.id)
        title = args.title

        create_files(id, title)
    except Exception as e:
        print(colored('\nfailed: {}\n'.format(e), 'red'))