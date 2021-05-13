#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-04-26 01:20:51
lastTime: 2021-04-26 01:52:05
LastAuthor: Do not edit
FilePath: /Turing/difflibDemo/test4.py
Description: 
version: 
'''


from P import Person, Car


# def test_person():
#     a = Person("Alice",age=21,favorites={"food":"eggs","movie":"Life of Brian"})
#     b = Person("Alice",age=21,favorites={"food":"eggs","movie":"Life of Brian"})
#     assert a==b

    
def test_car():
    c1=Car("Honda","Prius",2010)
    c2=Car("Honda","Prius",2010)
    assert c1==c2