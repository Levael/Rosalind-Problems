from pathlib import Path
import inspect
from typing import Any


def _caller_dir() -> Path:
    """
    Return the directory of the first stack frame outside this module.
    Falls back to the current working directory.
    """
    this_file = Path(__file__).resolve()
    for frame in inspect.stack()[1:]:
        fname = getattr(frame, "filename", None)
        if not fname:
            continue
        p = Path(fname).resolve()
        if p != this_file:
            return p.parent
    return Path.cwd()


def ReadInput(filename: str = "input.txt") -> str:
    """
    Read text from filename. If filename is relative, first try the caller's folder,
    then the current working directory. Returns file contents as a string.
    """
    if not filename:
        raise ValueError("ReadInput requires a non-empty filename.")

    path = Path(filename)
    if path.is_absolute() and path.exists():
        return path.read_text(encoding="utf-8").strip()

    caller_path = _caller_dir() / filename
    if caller_path.exists():
        return caller_path.read_text(encoding="utf-8").strip()

    cwd_path = Path.cwd() / filename
    if cwd_path.exists():
        return cwd_path.read_text(encoding="utf-8").strip()

    raise FileNotFoundError(
        f"ReadInput: file not found. Tried:\n"
        f" - {path} (as given)\n"
        f" - {caller_path} (relative to caller)\n"
        f" - {cwd_path} (relative to cwd)"
    )


def WriteOutput(result: Any, filename: str = "output.txt") -> str:
    """
    Accept any value, convert to a string and write to filename.
    - list/tuple -> join elements with spaces (useful for contest outputs).
    - otherwise str(result).
    Returns the string that was written.
    """
    if isinstance(result, (list, tuple)):
        out_str = " ".join(map(str, result))
    else:
        out_str = str(result)

    path = Path(filename)
    if not path.is_absolute():
        path = _caller_dir() / filename

    path.write_text(out_str, encoding="utf-8")
    return out_str