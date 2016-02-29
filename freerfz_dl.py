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
import urllib2
from distutils.spawn import find_executable
from distutils.version import LooseVersion

class DLCalls:
    def __init__(self):
        # regex for Klasse A calls
        self.acalls = "D([CDGHJ][0-9]|[BFKLM][1-9])[A-Z]{2,3}"
        self.ecalls = "DO[1-9][A-Z]{2,3}"
        self.pdffile = 'Rufzeichenliste_AFU.pdf'
        self.outfile = 'freecalls.txt'
        self.download_Rufzeichenliste()
        self.dlcalls = self.generiere_Rufzeichenliste()

    def out(self):
        print self.dlcalls
        return

    def download_Rufzeichenliste(self):
        url = 'http://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Telekommunikation/Unternehmen_Institutionen/Frequenzen/Amateurfunk/Rufzeichenliste/Rufzeichenliste_AFU.pdf?__blob=publicationFile&v=11'
        dl = False

        r = urllib2.urlopen(url)
        downloadlength = r.headers['content-length']

        try:
            fd = open(self.pdffile, 'rb')
            filelength = len(fd.read())
            fd.close()
            if int(downloadlength) != int(filelength):
                dl = True
        except IOError:
            dl = True

        if dl:
            print "Lade neues PDF runter."
            try:
                with open(self.pdffile, 'wb') as f:
                    f.write(r.read())
            except:
                print "Download Error"
        else:
            print "Rufzeichenliste braucht nicht erneut runter geladen zu werden."
        r.close()
        return

    def generiere_Rufzeichenliste(self):
        pdfgrep = find_executable("pdfgrep")
        if pdfgrep == None:
            print "Bitte installiere 'pdfgrep'."
            sys.exit(1)
        else:
            pdfgrepversioncall = pdfgrep + " -V"
            proc = subprocess.Popen(shlex.split(pdfgrepversioncall), stdout=subprocess.PIPE, shell=False)
            (out, err) = proc.communicate()
            pdfgrepversion = re.search(r"^This is pdfgrep version\s*([\d.]+)", out).group(1)
            if LooseVersion(pdfgrepversion) < LooseVersion("1.4.0"):
                print "pdfgrep Version %s enthält die benötigten Features nicht. Bitte installiere mindestens Version 1.4.0." % (pdfgrepversion)
                sys.exit(1)
        pdfgrepcall = pdfgrep +" -o \""+self.acalls+"\" "+self.pdffile
        print "Lese Rufzeichen aus der Rufzeichenliste aus."
        try:
            proc = subprocess.Popen(shlex.split(pdfgrepcall), stdout=subprocess.PIPE, shell=False)
            (out, err) = proc.communicate()
        except subprocess.CalledProcessError as e:
            print "Error bei pdfgrep. Beende Programm."
            print e.output
        return out.split()

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
        print "Generiere freie Klasse A Rufzeichen."
        allcalls = []
        for prefix in ['DB', 'DC', 'DD', 'DF', 'DG', 'DH', 'DJ', 'DK', 'DL', 'DM']:
        #for prefix in ['DO']:
            for number in range(10):
                for alpha in string.ascii_uppercase:
                    for bravo in string.ascii_uppercase:
                        call = prefix+str(number)+alpha+bravo
                        allcalls.append(call)
                        for charlie in string.ascii_uppercase:
                            suffix = alpha+bravo+charlie
                            if suffix in nonsuffix:
                                continue
                            call = prefix+str(number)+suffix
                            allcalls.append(call)
        diff = set(allcalls) - set(self.dlcalls)
        f = open(self.outfile, 'w')
        for c in sorted(diff):
            f.write("%s\n" % c)
        f.close()
        print "Freie Rufzeichen liegen in der Datei '%s'." % (self.outfile)
        return


if __name__ == "__main__":
    c = DLCalls()
    c.freecalls()


