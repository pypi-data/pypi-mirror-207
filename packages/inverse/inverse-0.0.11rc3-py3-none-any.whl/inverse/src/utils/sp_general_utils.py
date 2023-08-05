import os
from pathlib import Path


def create_dirs(dir):
    dir = Path(dir) if not isinstance(dir, Path) else dir

    if not os.path.exists(dir):
        os.makedirs(dir)