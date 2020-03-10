import functools
import os


def depends(file: str, exists: str = True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(ctx):
            fexists = os.path.exists(file)
            if fexists != exists:
                print(f"failed depends check. Not executing {func.__name__} task")
                return False
            return func(ctx)
        return wrapper
    return decorator
