
def get(obj, path: str, default=None):
    """
    Forgiving get dot prop.
    If some level doesn't exist, it returns the default.
    """
    value = obj
    for key in path.split('.'):
        if isinstance(value, list):
            index = int(key)
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


def strict_get(obj, path: str):
    """
    Strict get dot prop.
    If some level doesn't exist, it raises the apropriate exception.
    """
    value = obj
    for key in path.split('.'):
        if isinstance(value, list):
            value = value[int(key)]
        elif isinstance(value, dict):
            value = value[key]
        else:
            value = getattr(value, key)
    return value
