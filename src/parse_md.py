from pathlib import Path
from typing import Optional

import mistune


def parse_file(file: str) -> Optional[str]:
    """
    Returns the HTML code for the specified markdown file,
    or raises a FileNotFoundError if the file could not be found.
    """
    fp = Path("/blog") / file
    raw = fp.read_text()
    return mistune.markdown(raw)
