import argparse
import os

from zoterotex._sync import sync


def main():
    args = get_args()
    sync(**vars(args))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("sync",))
    parser.add_argument("library_type", choices=("library", "group"))
    parser.add_argument("library_id")
    parser.add_argument("out_file")
    parser.add_argument("--api-key", default=os.environ.get("ZOTERO_API_KEY", None))
    parser.add_argument("--log-level", choices=("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"), default="INFO")
    return parser.parse_args()


if __name__ == '__main__':
    main()
