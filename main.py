"""Entry program for make.fun news-image-20261117.

Writes the bundled front-page image to the output location as
``entry.png``. The image is a JPEG (the competition accepts PNG or JPEG,
told apart by the first bytes), so the file keeps the name ``entry.png``
while holding JPEG bytes.

The output directory comes from the ``MAKEFUN_OUTPUT_DIR`` environment
variable when it is set; otherwise the default ``/output`` directory is
used. The directory is created if it does not exist. The bundled image
is located relative to this file, so the program works from any working
directory. No network is used, and the output bytes are identical on
every run because the program only copies the bundled file.
"""

import os
import shutil
from pathlib import Path

IMAGE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def main() -> None:
    source = Path(__file__).resolve().parent / IMAGE_NAME
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / IMAGE_NAME
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
