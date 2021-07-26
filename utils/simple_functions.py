# simple_functions.py

from typing import List 


def check_all_true(actors, i=0) -> bool:
    if i < len(actors):
        if actors[i].consensus.resolve():
            check_all_true(actors, i + 1)
        else:
            return False
    return True


def return_true(): return True


def build_read_from_interface(interface):
    def read_from_interface(interface):
        return interface.read()

    return read_from_interface


def null_fn(*args, **kwargs):
    pass


def requires(resource_a, resource_b):
    assert resource_a is not None
    assert resource_b is not None