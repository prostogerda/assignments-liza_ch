#! /usr/bin/env python


from __future__ import division, print_function


def my_max(*args):
    for maxim in args:
        pass
    # In this case it's possible to use   maxim = None
    # instead of two previous lines (first iteration)
    for index in args:
        if index > maxim:
            maxim = index
    return maxim


def my_min(*args):
    for minim in args:
        pass
    for index in args:
        if index < minim:
            minim = index
    return minim
