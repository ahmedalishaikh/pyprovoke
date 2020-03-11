import functools
import json
import os

RCFILE = ".invokerc"


def _get_mtime_from_rcfile(path: str):
    if not os.path.exists(RCFILE):
        return None
    with open(RCFILE, "r") as fp:
        rc_obj = json.load(fp)
    try:
        return rc_obj["provoke"]["file_mtime_record"][path]
    except IndexError:
        return None


def _update_mtime_in_rcfile(path: str, mtime: int):
    if os.path.exists(RCFILE):
        with open(RCFILE, "r") as fp:
            rc_obj = json.load(fp)
    else:
        rc_obj = {}
    rc_obj.setdefault("provoke", {}).setdefault("file_mtime_record", {})[path] = mtime
    with open(RCFILE, "w") as fp:
        json.dump(rc_obj, fp)


def run_if_exists(path: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(ctx):
            if not os.path.exists(path):
                print(f"failed run_if_exists check. Not executing {func.__name__} task")
                return False
            return func(ctx)
        return wrapper
    return decorator


def run_if_not_exists(path: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(ctx):
            if os.path.exists(path):
                print(f"failed run_if_not_exists check. Not executing {func.__name__} task")
                return False
            return func(ctx)
        return wrapper
    return decorator


def run_if_changed(path: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(ctx):
            recorded_mtime = _get_mtime_from_rcfile(path)
            file_mtime = os.path.getmtime(path)
            if recorded_mtime is None or file_mtime != recorded_mtime:
                _update_mtime_in_rcfile(path, file_mtime)
                return func(ctx)
            else:
                print(f"failed run_if_changed check. Not executing {func.__name__} task")
                return False
        return wrapper
    return decorator
