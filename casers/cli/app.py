import argparse

from casers import __version__


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="casers",
        description=f"casers {__version__}",
    )
    parser.add_argument("-V", "--version", action="version", version=__version__)

    return parser.parse_args()


def run() -> None:
    _ = _parse_args()
