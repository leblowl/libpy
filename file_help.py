import os
import fnmatch
from lib_help import flatten

def read_range(filepath, s_ndx, e_ndx):    
    """
    Returns lines of file @ filepath between s_ndx and e_ndx exclusive
    """
    with open(filepath) as _file:
        snippet = []
        if e_ndx == -1:
            snippet = list(_file)
        else:
            snippet = [(num, line)
                       for num, line in enumerate(_file)
                       if num >= s_ndx and num <= e_ndx]
        return snippet

def read(filepath, n):
    """
    Returns first n lines of file @ filepath
    """
    return read_range(filepath, 0, n)

def write(filepath, content):
    _file = open(filepath, 'w+')
    _file.write(content)
    _file.close()

def find_file(root, filename):
    """
    Returns list of files that match filename under the given root directory. Searches recursively.
    """
    if filename:
        files = [[os.path.abspath(os.path.join(file_info[0], name)) for name in file_info[2] if fnmatch.fnmatch(name, filename)] 
                 for file_info
                 in os.walk(root)]

        return flatten(files)

def insert(filepath, index, value):
    """
    Inserts value as line @ index in file @ filepath if it doesn't already exist
    """
    contents = None
    with open(filepath, 'r+') as _file:
        contents = [line for line in _file]
        if contents[index] != value:
            contents.insert(index, value)
        _file.seek(0)
        _file.truncate()
        for line in contents:
            _file.write(line)

def delete(filepath, index):
    """
    Deletes lines @ index in file @ filepath
    """
    contents = None;
    with open(filepath, 'r+') as _file:
        contents = [line for line in _file]
        del contents[index]
        _file.seek(0)
        _file.truncate()
        for line in contents:
            _file.write(line)