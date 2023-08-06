"""Python utils for the open-reading-foundation GitHub org"""

import json
from pathlib import Path

ORF_UTILS_METADATA = Path(__file__).parent / "metadata.json"

with open(ORF_UTILS_METADATA, 'r', encoding="utf-8") as json_fh:
    __version__ = json.load(json_fh)["version"]
