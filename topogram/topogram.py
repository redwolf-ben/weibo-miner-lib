#!/usr/bin/env python
# -*- coding: utf-8 -*-

from processor import Processor
from processors.nlp import NLP
from corpus import Corpus
from utils import any2utf8

from datetime import datetime

import logging 
logger = logging.getLogger('topogram.Topogram')

try:
    import cPickle as _pickle
except ImportError:
    import pickle as _pickle

class Topogram:
    """
    base class to extract citations from text and generate networks of citations and words.
    This class should be instantiated to use a specific processing algorithms.
    """

    def add_citation_to_ignore(self, citation):
        """ Add a string to the list of citations to be ignored during processing. For instance, if you want to ignore a user (@justinbieber) while processing your tweets."""
        self.ignored_citations.append(citation)

    def __init__(self, corpus=Corpus, processors=[]):
        """
        Initialize a topogram from a corpus and a set of processors

        """
        logger.info("Init Topogram with %s processors"%len(processors))

        if not isinstance(corpus, Corpus):
            raise TypeError("Topogram arg 1 should be a Corpus instance")
        else :
            self.corpus = corpus

        # validate processors
        for i, process in enumerate(processors) : 
            if not isinstance(process[0], str):
                raise TypeError("Topogram arg 2 should be a tuple (str, Processor instance)")
            if not isinstance(process[1], Processor):
                raise TypeError("Topogram arg 2 should be a tuple (str, Processor instance)")

        self.processors = processors
        self.ignored_citations=[]

        # init  timeFrame
        self.start = None
        self.end = None


    def process(self):
        """ Process the whole corpus"""
        logger.info("Start processing the corpus")

        for i, row in enumerate(self.corpus):
            for j, process in enumerate(self.processors): 
                 row[ process[0] ] = process[1](row["text_column"])
            yield row

        logger.info("Corpus processing done")
