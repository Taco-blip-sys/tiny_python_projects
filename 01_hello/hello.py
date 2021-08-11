#!/usr/bin/env python3
"""
Author : TF <TF>
Date   : 2021-08-01
Purpose: Hello World
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Hello World',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--name',
                        help='The name to greet',
                        metavar='NAME',
                        type=str,
                        default='World')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(f'Hello, {args.name}!')



# --------------------------------------------------
if __name__ == '__main__':
    main()
