#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: LEGEND
since: 2024-05-13 03:46:58
lastTime: 2024-05-13 03:47:04
LastAuthor: Do not edit
FilePath: /Turing/13-协程/pytest/test_01.py
Description: 
version: 
'''

from aiohttp import web


async def hello(request):
    return web.Response(body=b"Hello, world")


def create_app():
    app = web.Application()
    app.router.add_route("GET", "/", hello)
    return app


async def test_hello(aiohttp_client):
    client = await aiohttp_client(create_app())
    resp = await client.get("/")
    assert resp.status == 200
    text = await resp.text()
    assert "Hello, world" in text