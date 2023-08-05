from fastmodel.backend.exception.exceptions import HTTPException
import os
from typing import List
import random
import string

def safe_join(directory: str, path: str) -> str:
    """Safely path to a base directory to avoid escaping the base directory.
    Borrowed from: werkzeug.security.safe_join"""
    _os_alt_seps: List[str] = [
        sep for sep in [os.path.sep, os.path.altsep] if sep is not None and sep != "/"
    ]

    if path == "":
        raise HTTPException(400)

    filename = os.path.normpath(path)
    fullpath = os.path.join(directory, filename)
    if (
            any(sep in filename for sep in _os_alt_seps)
            or os.path.isabs(filename)
            or filename == ".."
            or filename.startswith("../")
            or os.path.isdir(fullpath)
    ):
        raise HTTPException(403)

    if not os.path.exists(fullpath):
        raise HTTPException(404, "File not found")

    return fullpath


def generate_random_string(length: int):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


if __name__ == '__main__':
    print(generate_random_string(7))

    # safe_join()
