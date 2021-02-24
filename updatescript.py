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

from datetime import datetime
import sys
import platform
import time
import json
import re
import urllib.request

import credentials
import mwclient

masterwiki =  mwclient.Site('en.wikipedia.org')
masterwiki.login(credentials.username,credentials.password)

pagelist = masterwiki.pages["Category:Requests for unblock"]
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
