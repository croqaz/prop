from .path import process_path


def get(obj, path, default=None, sep='.'):
    """
    Forgiving get dot prop.
    If some level doesn't exist, it returns the default.
    """
    value = obj
    for key in process_path(path, sep):
        if isinstance(value, list):
            if isinstance(key, (str, bytes)):
                index = int(key, 10)
            else:
                index = key
            if index < len(value):
                value = value[index]
            else:
                return default
        elif isinstance(value, dict):
            if key in value:
                value = value[key]
            else:
                return default
        else:
            if hasattr(value, key):
                value = getattr(value, key)
            else:
                return default
    return value


def strict_get(obj, path, sep='.'):
    """
    Strict get dot prop.
    If some level doesn't exist, it raises the apropriate exception.
    """
    value = obj
    for key in process_path(path, sep):
        if isinstance(value, list):
            value = value[int(key, 10)]
        elif isinstance(value, dict):
            value = value[key]
        else:
            value = getattr(value, key)
    return value
