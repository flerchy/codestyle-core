#!/usr/bin/env python
"""ennui is an alternative command-line user-interface to enstaller (enpkg).

Usage:
    ennui (install | upgrade | remove) <package>...
    ennui install <package> [version]
    ennui upgrade
    ennui search <string>
    ennui info <package>
    ennui list (all | installed | outdated)
    ennui set-credentials
    ennui show-config
    ennui log
    ennui imports
    ennui version
    ennui help

Options:
    -h --help       Show this screen,
    --version       Show version of this tool.
"""

__version__ = '0.1alpha'

import sys
from docopt import docopt
from getpass import getpass
from sh import enpkg


aggregated = ""


def userpass_interact(char, stdin):
    """Do fancy things to interact with `enpkg --userpass`."""
    global aggregated
    sys.stdout.write(char.encode())
    aggregated += char
    if aggregated.endswith("Email (or username): "):
        user_in = raw_input()
        stdin.put(user_in + "\n")
    elif aggregated.endswith("Password: "):
        user_in = getpass('')
        stdin.put(user_in + "\n")


def dispatch(arguments):
    """Take the command-line arguments and translate them into enpkg
    arguments.
    """
    if arguments['help']:
        print __doc__
    elif arguments['version']:
        print __version__
    elif arguments['show-config']:
        print enpkg('--config')
    elif arguments['log']:
        print enpkg('--log')
    elif arguments['imports']:
        print enpkg('--imports')
    elif arguments['set-credentials']:
        p = enpkg('--userpass', _out=userpass_interact, _out_bufsize=0, _tty_in=True)
        p.wait()
    elif arguments['info']:
        print enpkg('--info', arguments['<package>'])
    elif arguments['search']:
        print enpkg('--search', arguments['<string>'])
    elif arguments['list']:
        if arguments['all']:
            print enpkg('--search')
        elif arguments['installed']:
            print enpkg('--list')
        elif arguments['outdated']:
            print enpkg('--whats-new')
    elif arguments['install']:
        if arguments['version']:
            print enpkg(arguments['<package>'], arguments['version'])
        else:
            print enpkg(arguments['<package>'])
    elif arguments['remove']:
        print enpkg('--remove', arguments['<package>'])
    elif arguments['upgrade']:
        if len(arguments['<package>']) == 0:
            whats_new = enpkg('--whats-new')
            lines = whats_new.strip().split('\n')
            if lines[2].strip() == "no new version of any installed package is available":
                for line in lines:
                    print line
            else:
                lines = lines[2:]  # discard header
                packages = [line.split()[0] for line in lines]
                print enpkg(packages)
        else:
            print enpkg(arguments['<package>'])


def main():
    arguments = docopt(__doc__, version=__version__)
    dispatch(arguments)


if __name__ == '__main__':
    main()
