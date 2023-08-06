import os
import re
from dataclasses import dataclass, fields


@dataclass
class ZoterotexHeader:
    library: str
    version: int
    retrieved: str
    zoterotek: str

    def __post_init__(self):
        self.version = int(self.version)

    def __str__(self):
        serialized = ", ".join(f"{field.name}: {getattr(self, field.name)}" for field in fields(self))
        return f"% {serialized}"

    @classmethod
    def parse(cls, s):
        pattern = "^% " + ", ".join(rf"({field.name}): (.*?)" for field in fields(cls)) + "$"
        match = re.search(pattern, s.strip(), flags=re.IGNORECASE)
        if not match:
            raise ValueError
        key_value_pairs = dict(zip(match.groups()[0::2], match.groups()[1::2]))
        return cls(**key_value_pairs)

    @classmethod
    def from_file(cls, filename):
        if not os.path.exists(filename):
            return None

        with open(filename) as f:
            return cls.parse(f.readline().strip())
