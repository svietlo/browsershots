# Copyright (C) 2006 Johann C. Rocholl <johann@browsershots.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Display recent screenshots for a given website.
"""

__revision__ = '$Rev$'
__date__ = '$Date$'
__author__ = '$Author$'

from shotserver03.interface import xhtml
from shotserver03 import database

def write():
    """
    Write XHTML div with recent screenshots.
    """
    database.connect()
    try:
        xhtml.write_open_tag('div', _id="screenshots")
        for row in database.screenshot.select_recent(req.params.website):
            hashkey = row[0]
            prefix = hashkey[:2]
            xhtml.write_tag('img', src="/png/148/%s/%s.png" % (prefix, hashkey))
        xhtml.write_close_tag_line('div') # id="screenshots"
    finally:
        database.disconnect()
