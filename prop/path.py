def process_path(path, sep='.'):
    if isinstance(path, (tuple, list)):
        return path
    elif isinstance(path, str):
        return path.split(sep)
    else:
        raise TypeError(f'Invalid path type: {type(path)}')
