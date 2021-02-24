# -*- coding: utf-8 -*-
"""
(C) 2020 DeltaQuad (enwp.org/User:DeltaQuad)
This file is part of DeltaQuadBot.
DeltaQuadBot is free software: you can redistribute it and/or modify
it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
DeltaQuadBot is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU AFFERO GENERAL PUBLIC LICENSE for more details.
You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
along with DeltaQuadBot. If not, see <https://www.gnu.org/licenses/agpl.txt>.
"""

from http.cookiejar import MozillaCookieJar
import sys, os, requests
import platform
import time
import json
import re
import traceback
import urllib.request

from mwclient import Site
import login

cookies_file = '/data/project/deltaquad-bots/int-admin-cookies.txt'

cookie_jar = MozillaCookieJar(cookies_file)
if os.path.exists(cookies_file):
    # Load cookies from file, including session cookies (expirydate=0)
    cookie_jar.load(ignore_discard=True, ignore_expires=True)
print('We have %d cookies' % len(cookie_jar))

connection = requests.Session()
connection.cookies = cookie_jar  # Tell Requests session to use the cookiejar.

masterwiki =  Site('en.wikipedia.org', pool=connection)
print("Login status: ")
print(masterwiki.logged_in)
if not masterwiki.logged_in:
	masterwiki.login(login.username,login.password)

# Save cookies to file, including session cookies (expirydate=0)
print(connection.cookies)
cookie_jar.save(ignore_discard=True, ignore_expires=True)

pagelist = masterwiki.pages["User:AmandaNP/scriptcopy.js"]
pagelist = pagelist.split("\n")

for wikipage in pagelist:
    wikipage = wikipage.split(",")
    postpage = masterwiki.pages[wikipage[0]]
    source = wikipage[1]
    website = urllib.request.urlopen(source)
    webtext=website.read()
    if postpage.text == webtext:continue


    #Save page
    postpage.save(webtext, "Manual - Updating code to latest version on " + source)
