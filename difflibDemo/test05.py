#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2021-04-26 01:59:10
lastTime: 2021-04-26 01:59:10
LastAuthor: Do not edit
FilePath: /Turing/difflibDemo/test05.py
Description: 
version: 
'''

import pytest
import numpy as np

@pytest.mark.array_compare
def test_succeeds():
    return np.arange(3 * 5 * 4).reshape((3, 5, 4))
