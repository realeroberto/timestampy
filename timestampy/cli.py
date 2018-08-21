# -*- coding: utf-8 -*-

"""Console script for timestampy."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for timestampy."""
    click.echo("Replace this message by putting your code into "
               "timestampy.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
