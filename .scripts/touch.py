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
    # -- Source location
    src_folder = "leetcode"
    tst_folder = "tests"

    # -- Templates --
    template_source_file = "./.scripts/TEMPLATE_SRC"
    template_source_file_name = "p{id:0>4d}_{title}.py"
    template_test_file = "./.scripts/TEMPLATE_TST"
    template_test_file_name = "test_" + template_source_file_name

    # -- Verification
    valid_domains = {"leetcode.com"}
    verify_url = True
    verify_path = True

    # -- Editor --
    editor = "code"
    open_editor = True


def extract_title(url):
    path = urlparse(url).path

    # drop trailing slash
    path = path[:-1] if path[-1] == "/" else path
    return os.path.split(path)[-1]


def file_name(id, title, kind="src"):
    """
    Generates file name from problem id and title.
    """
    fn_template = conf.template_source_file_name
    if kind == "tst":
        fn_template = conf.template_test_file_name

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
            print(colored(f"{ex.args[0]}: {url}", "red"))
            return False
    return True


def verify_path(file_path):
    if conf.verify_path:
        if os.path.isfile(file_path):
            print(colored("Already exists: {file}".format(file=file_path), "red"))
            return False
    return True


def src_template(id, title):
    with open(conf.template_source_file, mode="r") as f:
        template = f.read()
        return template


def tst_template(id, title):
    with open(conf.template_test_file, mode="r") as f:
        template = f.read()
        return template.format(
            src=file_name(id, title, "src")[:-3],  # without .py extension
            method="solve",
        )


def create_files(id: str, url: str):
    title = extract_title(url)
    src = os.path.join(conf.src_folder, file_name(id, title, "src"))
    tst = os.path.join(conf.tst_folder, file_name(id, title, "tst"))

    valid = verify_url(url)
    valid = verify_path(src) and valid
    valid = verify_path(tst) and valid

    if not valid:
        return None

    print(colored("Created:", "green"))
    with open(src, "w") as f:
        f.write(src_template(id, title))
        print(colored(f"  {src}", "green"))

    with open(tst, "w") as f:
        f.write(tst_template(id, title))
        print(colored(f"  {tst}", "green"))

    return src, tst


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

        out = create_files(id, url)
        if out:
            refresh_markdown("README.md", False, True)
            print(colored("\nUpdated:\n  README.md\n", "green"))

            src, tst = out
            if conf.open_editor:
                os.system(f"{conf.editor} {src}")
                os.system(f"{conf.editor} {tst}")

    except Exception as e:
        print(colored("\nfailed: {}\n".format(e), "red"))
