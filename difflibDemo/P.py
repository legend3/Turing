#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-04-26 01:23:40
lastTime: 2021-04-26 01:52:38
LastAuthor: Do not edit
FilePath: /Turing/difflibDemo/P.py
Description: 
version: 
'''
import pytest_diff

class Person():
    def __init__(self, name, age, favorites):
        self.name=name
        self.age=age
        self.favorites=favorites

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

@pytest_diff.registry.register(Car)
def diff(x, y):
    return [
               f"{x.make} vs {y.make}",
               f"{x.model} vs {y.model}",
               f"{x.year} vs {y.year}",
           ]