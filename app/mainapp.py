#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
import math
from config import basedir


class MainApp:
    """ This is a Main Application
    """
    def __init__(self, trainingdir, inputdoc):
        self.trainingdir = trainingdir
        self.inputdoc = inputdoc

        filename = self.trainingdir + self.inputdoc
        # self.f = open(filename)
        self.f = codecs.open(filename, 'r', 'iso8859-1')
        # print(self.f.readline())

    def extract(self):
        content = self.f.readline()
        # print(content)
        return content


if __name__ == '__main__':
    # training_dir = os.path.join(basedir, 'app', 'static', 'app', 'app-kb', 'app-kb-train')
    training_dir = os.path.join(basedir, 'app', 'static', 'app', 'app-kb', 'app-kb-train', '00010Preface')
    training_dir = training_dir + os.sep
    doc = '01.txt'
    mba = MainApp(training_dir, doc)
    print(mba.extract())
