#!/usr/bin/python
import os, sys, string, fnmatch

def coroutine(func):
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
	g.next()
	return g
    return start

@coroutine
def echo(target):
    while True:
        line = (yield)
        target.send(line)

@coroutine
def grep(pattern, target):
    while True:
        line = (yield)
        if pattern in line:
            target.send(line)

@coroutine
def awk():
    while True:
        line = (yield)
        pmatch = line.split()
        print pmatch[3]

