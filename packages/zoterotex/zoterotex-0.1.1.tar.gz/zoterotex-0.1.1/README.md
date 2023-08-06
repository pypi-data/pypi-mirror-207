# zoterotex

Wrapper for [`pyzotero`](https://github.com/urschrei/pyzotero) that keeps a BibTeX file in sync with a Zotero library.

## Setup

### API Key

You'll need an API key to use `zoterotex`, which can be created in
[your Zotero account](https://www.zotero.org/settings/keys/new).

### Installation

```bash
pip install zoterotex
```


## Example usage

### For a user library

You can retrieve your userid from [your Zotero keys settings](https://www.zotero.org/settings/keys). For example, if 
your username is 54321, you can sync with:

```bash
zoterotex sync user 54321 myuser.bib --api-key aabbccdd11223344
```

### For a group library

If you navigate to [your Zotero groups], you can grab a group ID from the url. For example, group
12345678 has the URL https://www.zotero.org/groups/12345678/my_group_name, and you can sync like so:

```bash
zoterotex sync group 12345678 mygroup.bib --api-key aabbccdd11223344
```
