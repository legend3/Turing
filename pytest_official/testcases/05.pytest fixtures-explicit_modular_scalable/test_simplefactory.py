#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2020-11-29 15:53:35
lastTime: 2020-11-29 15:53:47
LastAuthor: Do not edit
FilePath: /Turing/pytest_official/testcases/05.pytest fixtures-explicit_modular_scalable/test_simplefactory.py
Description: 
version: 
'''


import pytest


@pytest.fixture
def smtp_connection():
    import smtplib

    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0  # for demo purposes