# -*- coding: utf-8 -*-
import re
import traceback
import json 
import numpy as np
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def getW2V(index_set, embedding_matrix):
    w2v_v = []
    for item in index_set:
        temp = []
        for n in item:
            temp.append(embedding_matrix[n])
        w2v_v.append(temp)
    w2v_v = np.array(w2v_v)
    return w2v_v

def read_json_file(filename):
    whole = []
    count = 0
    with open(filename) as fin:
        for eachline in fin:
            if eachline.strip() == "NULL":
                continue
            eachline = eachline.replace('\r\n', '')
            eachline = eachline.strip()
            pa = re.compile(r'"content":\s?"(.*?","\w)')
            for s in pa.findall(eachline):
                s = s[:-4]
                s_fix = s.replace("\"","")
                eachline = eachline.replace(s,s_fix)
            eachline = eachline.replace('\\','\\\\') 
            #eachline = eachline.encode('utf8')
            try:
                data = json.loads(eachline)
                whole.append(data)
            except:
                count += 1
                #print(eachline)
                #traceback.print_exc()
    logger.debug('Errors: %s' % str(count))
    return whole

    
def filter_word_count(w,wordset,wordlist,count=100):
    if w in wordset:
        if wordset[w]>=count:
            wordlist.append(w)
    return wordlist 