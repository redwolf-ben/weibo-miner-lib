#!/usr/bin/env python
# -*- coding: utf-8 -*-

from topogram.processor import Processor

import re

class Regexp(Processor):

    def __init__(self, regexp):
        
        if type(regexp) is str : 
            self.regexp = self.compile_regexp(regexp)
        else : 
            raise ValueError("topogram : Regexp arg should be a str")  

    def compile_regexp(self, regexp):
        """ compile a regexp only once to gain time during processing """
        return re.compile(regexp, re.UNICODE)

    def __call__(self, content):
        """ 
            Extract all citations from a given text. 
            Return a list of citations
        """
        return self.regexp.findall(content)
