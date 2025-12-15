import argparse
import argparse
from commands import register_all
from logging_config import setup_logging
import logging

"""
Automated utility created to allow the bulk modification of assets in a Trail database.

Created by Sam Lane
"""

def main():
    parser = argparse.ArgumentParser(
        prog="trail-api-utility.py",
        description="Use this utility to bulk modify items in a Trail environment.",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without making changes"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    register_all(subparsers)

    args = parser.parse_args()

    setup_logging(args.verbose)

    logging.getLogger(__name__).debug("CLI arguments parsed")

    args.handler(args)

if __name__ == '__main__':
    main()






