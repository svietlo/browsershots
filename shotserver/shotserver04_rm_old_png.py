#!/usr/bin/env python
# Delete old PNG files
#
# This script expects a list of candidates on stdin, like this:
# /var/www/v04.browsershots.org/png/160/74/749a5c7602d6de93d9a5bfdc2e7db1a9.png
# /var/www/v04.browsershots.org/png/160/74/742d8deb15f0cf2cd0a347f7dc3c58f7.png
# /var/www/v04.browsershots.org/png/160/74/7492c8add13e09205a3c788d47f9e599.png
#
# You can use the following command to find good candidates:
# find /var/www/v04.browsershots.org/png/160 -atime +10

import sys
import os
import glob
import time

NOW = time.time()
EXPIRE_DAYS = 10
EXPIRE = NOW - EXPIRE_DAYS * 24 * 3600
FOLDERS = glob.glob('/var/www/v04.browsershots.org/png/*')


def png_filename(folder, hashkey):
    return os.path.join(folder, hashkey[:2], hashkey + '.png')


def _main():
    for candidate in sys.stdin:
        basename = os.path.basename(candidate.rstrip())
        if len(basename) != 36:
            print basename, len(basename)
        hashkey = basename[:32]
        filenames = [png_filename(folder, hashkey) for folder in FOLDERS]
        filenames = filter(os.path.exists, filenames)
        atimes = [os.stat(filename).st_atime for filename in filenames]
        if max(atimes) > EXPIRE:
            continue
        print hashkey, len(atimes), max(atimes)


if __name__ == '__main__':
    _main()