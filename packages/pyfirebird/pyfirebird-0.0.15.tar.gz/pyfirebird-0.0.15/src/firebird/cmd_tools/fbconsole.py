#!/usr/bin/env python
# -*- coding: UTF-8 -*-

####################################################################################
# Command line tool to launch firebird console
# Usage:
#     fbconsole args
# The args format is the same as you pass to manage.py in a regular django app
####################################################################################

import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(
        description='Firebird Console'
    )
    parser.add_argument(
        "-cd", "--config-dir", type=str, default=os.path.expanduser("~/.firebird"), required=False,
        help="Configuration directory"
    )
    parser.add_argument(
        "-a", "--ip-address", type=str, default="0.0.0.0", help="binding ip address"
    )
    parser.add_argument(
        "-p", "--port", type=str, default="80", help="binding port"
    )
    args = parser.parse_args()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firebirdconsole.firebirdconsole.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
