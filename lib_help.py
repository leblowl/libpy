import itertools
import json
from functools import reduce
from collections import OrderedDict

def update_in(dict_old, key, update_func):
    dict_new = dict(dict_old)
    dict_new[key] = update_func(dict_new[key])
    return dict_new

def swap_in(dict, key, update_func):
    dict[key] = update_func(dict[key])
    return dict

def reset_in(dict, key, value):
    dict[key] = value
    return dict

def assoc_in(dict_old, key, value):
    dict_new = dict(dict_old)
    dict_new[key] = value
    return dict_new

def assoc_in_many(dict1, dict2):
    dict1.update(dict2)
    return dict1

def flatten(nested_list):
    return list(itertools.chain.from_iterable(nested_list))

def inc(val):
    return val + 1

def apply(f, *args):
    return f(*args)

def maybe(f, *args):
    if all(arg is not None for arg in args):
        return f(*args)

def do(val, *funcs):
    return reduce(lambda x, y: y(x), funcs, val)

def format(data):
    return json.dumps(OrderedDict(sorted(data.items())), indent=4)
