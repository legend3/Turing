#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: Do not edit
lastTime: 2020-08-03 00:55:23
LastAuthor: Do not edit
FilePath: \Turing\pytest_official\02UsageAndInvocations\run.py
Description: 
version: 
'''


import pytest
from pytest import ExitCode


args = ['-v', 'l', 'test_example.py::test_ok']
print(pytest.main(args))
# if pytest.main(args) == ExitCode.OK:
#     print('ok')


