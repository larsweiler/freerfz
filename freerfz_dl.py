#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Lars Weiler DC4LW"
__license__ = "THE NERD-WARE LICENSE (Revision 1)"
__version__ = "0.9"
__maintainer__ = "Lars Weiler"
__email__ = "dc4lw@darc.de"

'''
-----------------------------------------------------------------------------
"THE NERD-WARE LICENSE" (Revision 1):
<dc4lw@darc.de> wrote this file. As long as you retain this notice
you can do whatever you want with this stuff. If we meet some day, and you
think this stuff is worth it, you can buy me a softdrink or some
food in return.
Lars Weiler
-----------------------------------------------------------------------------
'''

'''
Benötigt das Verzeichnis der zugeteilten deutschen Amateurfunkrufzeichen und
ihrer Inhaber (Rufzeichenliste)
http://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Telekommunikation/Unternehmen_Institutionen/Frequenzen/Amateurfunk/Rufzeichenliste/Rufzeichenliste_AFU.pdf?__blob=publicationFile&v=10
'''

import os
import sys
import subprocess
import shlex
import string
import re

class DLCalls:
    def __init__(self):
        # regex for Klasse A calls
        self.acalls = "D([CDGHJ][0-9]|[BFKLM][1-9])[A-Z]{2,3}"
        pdfgrepcall = "/usr/local/bin/pdfgrep -o \""+self.acalls+"\" Rufzeichenliste_AFU.pdf"
        args = shlex.split(pdfgrepcall)
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
        (out, err) = proc.communicate()
        self.dlcalls = out.split()
    def out(self):
        print self.dlcalls
    def nonqgroup(self):
        q = []
        # no Q-Groups from QOA-QUZ allowed as suffix
        for a in string.uppercase[14:21]:
            for b in string.ascii_uppercase:
                q.append("Q"+a+b)
        return q
    def freecalls(self):
        pattern = re.compile(self.acalls)
        # these suffixes are not allowed
        nonsuffix = ["SOS", "XXX", "TTT", "YYY", "DDD", "JJJ", "MAYDAY", "PAN"] + self.nonqgroup()
        print nonsuffix
        f = open('freecalls.txt', 'w')
        for prefix in ['DB', 'DC', 'DD', 'DF', 'DG', 'DH', 'DJ', 'DK', 'DL', 'DM']:
            for number in range(10):
                for alpha in string.ascii_uppercase:
                    for bravo in string.ascii_uppercase:
                        call = prefix+str(number)+alpha+bravo
                        if pattern.match(call):
                            if call not in self.dlcalls:
                                f.write("%s\n" % call)
                        for charlie in string.ascii_uppercase:
                            suffix = alpha+bravo+charlie
                            if suffix in nonsuffix:
                                continue
                            call = prefix+str(number)+suffix
                            if pattern.match(call):
                                if call not in self.dlcalls:
                                    f.write("%s\n" % call)
        f.close()


if __name__ == "__main__":
    c = DLCalls()
    c.freecalls()


