# simple_functions.py

from typing import List 

from primitives.resources import Actor, Interface


def check_all_true(actors: List[Actor], i=0) -> bool:
    if i < len(actors):
        if actors[i].consensus.resolve():
            check_all_true(actors, i + 1)
        else:
            return False
    return True


def return_true(): return True


def build_read_from_interface(interface: Interface):
    def read_from_interface(interface):
        return interface.read()

    return read_from_interface