from bs4 import BeautifulSoup
from lxml import etree
from io import StringIO, BytesIO
import urllib2, re, os

class nameslist:
    def getnames(self, link):
        allnames = []
        for i in link:
            #self.getallnames(i)
            list = "file://" + i
            page = urllib2.urlopen(list)
            soup = BeautifulSoup(page.read(), 'lxml')
            for row in soup.findAll("tr"):
                for all in row.findNext('td'):
                    for a1 in all.findNext('td'):
                        allnames.append(a1.text)

        return allnames


