#!/usr/bin/env python3
"""
Creates problem and test templates.
Refreshes problem list in README.md.
"""

import os
import requests
from urllib.parse import urlparse
from argparse import ArgumentParser
from termcolor import colored
from genmd import refresh_markdown


class conf:
    problem_template_file = "./scripts/PROBLEM_TEMPLATE"
    problem_test_template_file = "./scripts/PROBLEM_TEST_TEMPLATE"
    verify_url = True
    verify_path = True
    valid_domains = {"leetcode.com"}


def extract_title(url):
    path = urlparse(url).path

    # drop trailing slash
    path = path[:-1] if path[-1] == "/" else path
    return os.path.split(path)[-1]


def file_name(id, title, kind="src"):
    """ Generates file name from problem id and title """
    fn_template = "p{id:0>4d}_{title}.py"
    if kind == "tst":
        fn_template = "test_" + fn_template

    return fn_template.format(id=id, title=title.replace("-", "_"))


def verify_url(url):
    if conf.verify_url:
        try:
            domain = urlparse(url).netloc
            if domain not in conf.valid_domains:
                raise Exception("Invalid domain")

            r = requests.get(url, timeout=3)
            if r.status_code != 200:
                raise Exception("Bad url")

        except Exception as ex:
            print(
                colored("{reason}: {link}".format(link=url, reason=ex.args[0]), "red")
            )
            return False
    return True


def verify_path(file_path):
    if conf.verify_path:
        if os.path.isfile(file_path):
            print(colored("Already exists: {file}".format(file=file_path), "red"))
            return False
    return True


def src_template(id, title):
    with open(conf.problem_template_file, mode="r") as f:
        template = f.read()
        return template


def tst_template(id, title):
    with open(conf.problem_test_template_file, mode="r") as f:
        template = f.read()
        return template.format(
            src=file_name(id, title, "src")[:-3],  # without .py extension
            method="solve",
        )


def create_files(id, url):
    title = extract_title(url)
    src = os.path.join("leetcode", file_name(id, title, "src"))
    tst = os.path.join("tests", file_name(id, title, "tst"))

    valid = verify_url(url)
    valid = verify_path(src) and valid
    valid = verify_path(tst) and valid

    if not valid:
        return False

    with open(src, "w") as f:
        f.write(src_template(id, title))
        print(colored("Created {}".format(src), "green"))

    with open(tst, "w") as f:
        f.write(tst_template(id, title))
        print(colored("Created {}".format(tst), "green"))

    return True


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--skip-verification",
        action="store_true",
        help="skip file and url verification",
    )
    parser.add_argument("id")
    parser.add_argument("url")
    args = parser.parse_args()

    conf.verify_url = not args.skip_verification
    conf.verify_path = not args.skip_verification

    try:
        # we don't want to parse HTML and extract the id
        # from the page, because it goes against
        # the leetcode usage policy
        id = int(args.id)
        url = args.url

        if create_files(id, url):
            refresh_markdown("README.md", False, True)
            print(colored("Updated README.md\n", "green"))
    except Exception as e:
        print(colored("\nfailed: {}\n".format(e), "red"))
