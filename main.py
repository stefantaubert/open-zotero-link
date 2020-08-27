from argparse import ArgumentParser
from re import match
from subprocess import Popen

from pyperclip import waitForNewPaste

_pattern = "zotero://select/library/items/.*\n"

def openzotero(zotero: str, profile: str, url: str):
    Popen([zotero, "-p", profile, "--url", url], stdin=None, stdout=None, stderr=None, close_fds=True)

def is_zotero_link(text: str):
    res = match(_pattern, text)
    return res != None

def run(zotero: str, profile: str, logging: bool):
    if logging: print(zotero, profile)
    while True:
        x = waitForNewPaste()
        if logging: print(f"received: {x}")

        if is_zotero_link(x):
            if logging: print(f"sent: {x}")
            cleaned = x.rstrip()
            openzotero(zotero, profile, cleaned)

if __name__ == "__main__":
    main_parser = ArgumentParser()
    main_parser.add_argument("--zotero", type=str, help="Location of zotero exec", default="/opt/Zotero_linux-x86_64/zotero")
    main_parser.add_argument("--profile", type=str, help="Name of the profile", default="default")
    main_parser.add_argument("--logging", action="store_true")
    args = main_parser.parse_args()
    run(args.zotero, args.profile, args.logging)
