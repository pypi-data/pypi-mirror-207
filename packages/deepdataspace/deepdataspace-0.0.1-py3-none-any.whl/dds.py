#! python

import click

"""
dds.py

This script starts the dds tool.

Usage: dds.py [OPTIONS] [DATA_DIR]

Options:
  --quickstart    Quick start dds with sample datasets instead of a specified
                  DATA_DIR, default false. This overwrites the DATA_DIR
                  argument.
  -V, --verbose   Display detailed logs on console, default false.
  -P, --public    Enable public access from your network neighbors, default
                  false. This sets the service host by an auto-detected
                  outward IP address.
  --host TEXT     Set the http service host. This overwrites the '--public'
                  flag.
  --port INTEGER  Set the http service port, default 8765.
  --reload        Auto reload service on code change, for development only.
  --help          Show this message and exit.
"""


@click.command("dds")
def main():
    click.echo("coming soon...")


if __name__ == "__main__":
    main()
