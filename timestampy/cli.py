# -*- coding: utf-8 -*-

"""Console script for timestampy."""
import sys
import click

import inotify.adapters
from inotify.constants import *
from subprocess import call
import os

@click.command()
@click.option('--f', default='~/timestampy')
def main(f):
    f = os.path.expanduser(f)

    i = inotify.adapters.Inotify()
    i.add_watch(f, mask = IN_CREATE | IN_MODIFY | IN_MOVED_TO)

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event

        print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
              path, filename, type_names))

        (_, file_extension) = os.path.splitext(filename)
        if not file_extension == ".ots":
            ots_file = os.path.join(path, filename + ".ots")
            if os.path.exists(ots_file):
                os.remove(ots_file)
            # create timestamp
            call(["ots", "stamp", os.path.join(path, filename)])
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

#vim: ai ts=4 sts=4 et sw=4 ft=python
