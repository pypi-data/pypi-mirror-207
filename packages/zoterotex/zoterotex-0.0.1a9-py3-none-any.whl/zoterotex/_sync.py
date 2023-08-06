import logging
import os
from datetime import datetime

import bibtexparser
from pyzotero.zotero import Zotero

import zoterotex
from zoterotex._header import ZoterotexHeader


def sync(action, library_id, out_file, library_type, api_key, log_level):
    logging.basicConfig(level=log_level)
    if not api_key:
        raise ValueError("Must provide Zotero API key with --api-key or environment variable $ZOTERO_API_KEY")
    logging.info(f"Retrieving library...")
    library = Zotero(library_id, library_type, api_key)
    write_bibtex(library, out_file)


def write_bibtex(library, out_file):
    try:
        header = ZoterotexHeader.from_file(out_file)
        if header.library == library.library_id and header.version == library.last_modified_version():
            logging.info(f"No updates since version {header.version} (retrieved on {header.retrieved}). Quitting.")
            return
    except ValueError:
        pass

    bibtex_database = library.items(format="bibtex")

    if "/" in out_file:
        os.makedirs(os.path.dirname(out_file), exist_ok=True)

    temp_file = f"{out_file}.tmp"
    with open(temp_file, "w") as f:
        header = ZoterotexHeader(
            library=library.library_id,
            version=library.last_modified_version(),
            retrieved=f"{datetime.now().astimezone():%Y-%m-%d %X %Z}",
            zoterotek=zoterotex.__version__
        )
        print(str(header), file=f)
        print(f"% This file was automatically generated. Do not update manually!", file=f)
        print(f"", file=f)
        bibtexparser.dump(bibtex_database, f)
        logging.info(f"Wrote BibTeX library to {out_file}")
    os.rename(temp_file, out_file)
