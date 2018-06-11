# -*- coding: utf-8 -*-
from project_demo.tools.fenci import *
from collections import *

class textPandas:
    def __init__(self, textdf, col, targetcol=None):
        self.textdf = textdf
        self.col = col
        self.targetcol = targetcol
        
    def text2list(self,targetcol,isjieba=False,**kargs):
        self.targetcol = targetcol

        if isjieba:
            self.textdf[targetcol] = self.textdf[self.col].apply(lambda x:jieba_cut_3(x,**kargs))
        else:
            self.textdf[targetcol] = self.textdf[self.col].apply(lambda x:x.split())
        return self
    
    def __filterWordCount(self, w, stopwords, count):
        if w in self.wordset and w not in stopwords:
            if self.wordset[w]>=count:
                self.temp.append(w)
                
    def getWordCount(self):
        self.wordset = defaultdict(int)
        for eachline in self.textdf[self.targetcol]:
            if type(eachline) == type('s'):
                self.wordset[eachline] += 1
            elif type(eachline) == type([]) or type(eachline) == type(()):
                for w in eachline:
                    self.wordset[w] += 1
                    
        return self
        
    def getTextdataby(self,by,count=1):
        tokenlist = []
        total = []
        for rgid, group in self.textdf.groupby(by):
            self.temp = []
            for text in group[self.targetcol]:
                if type(text) == type('a'):
                    self.__filterWordCount(text,{},count)
                elif type(text) == type([]) or type(text) == type(()):
                    for w in text:
                        self.__filterWordCount(w,{},count)
            tokenlist.append(' '.join(self.temp))
            total.append(self.temp)
        return total,self.wordset,tokenlist

    def getTextdata(self,count=1):
        tokenlist = []
        total = []
        
        for eachline in self.textdf[self.targetcol]:
            self.temp = []
            if type(eachline) == type('a'):
                self.__filterWordCount(text,{},count)
            elif type(eachline) == type([]) or type(eachline) == type(()):
                for w in eachline:
                    self.__filterWordCount(w,{},count)
            tokenlist.append(' '.join(self.temp))
            total.append(self.temp)
        
        return total,self.wordset,tokenlist