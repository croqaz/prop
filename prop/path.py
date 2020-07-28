def process_path(path):
    if isinstance(path, (tuple, list)):
        return path
    elif isinstance(path, str):
        return path.split('.')
    elif isinstance(path, bytes):
        return path.split(b'.')
    else:
        raise TypeError(f'Invalid path type: {type(path)}')
