#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict
import math # sqrt

###############################################################################
def read_frequency(filename):

    fin = open(filename, 'r')
    freqs = defaultdict(int)
    for line in fin.readlines():
        temp = line.split('\t')
        freqs[temp[0]] = temp[1]

    return freqs

###############################################################################
def calc_tscore(filename, unigrams, unigram_context, uni_N, cutoff):

    t_scores = defaultdict(int)
    
    fin = open(filename, 'r')
    bigrams = defaultdict(int)
    for line in fin.readlines():
        temp = line.split('\t')
        O = int(temp[2])
        E = int(unigram_context[temp[0]]) * int(unigrams[temp[1]]) / int(uni_N)
        t = (O - E) / math.sqrt(O)
        if O >= CUTOFF and temp[1] not in temp[0] and t > 0:
            t_scores[(temp[0],temp[1])] = t
        E = int(unigram_context[temp[1]]) * int(unigrams[temp[0]]) / int(uni_N)
        t = (O - E) / math.sqrt(O)
        if O >= CUTOFF and temp[0] not in temp[1] and t > 0:
            t_scores[(temp[1],temp[0])] = t

    t_scores = dict(sorted(t_scores.items()))    
  
    return t_scores

###############################################################################
def print_tscore(filename, t_scores):
    
    fout = open(filename, 'w')

    for word_tuple, t_score in t_scores.items():
        w1, w2 = word_tuple
        print('%s\t%s\t%.3f'%(w1, w2, t_score), file=fout)
 
###############################################################################
if __name__ == "__main__":

    CUTOFF = 5 # 공기빈도가 이 값 이상인 경우만 t점수를 계산
    
    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    for input_file in sys.argv[1:]:
        
        print( 'processing %s' %input_file, file=sys.stderr)

        file_stem = input_file
        pos = input_file.find(".")
        if pos != -1:
            file_stem = input_file[:pos] # ex) "2017.2gram" -> "2017"
    
        print("\tLoading %s.1gram" %file_stem, file=sys.stderr)
        unigrams = read_frequency(file_stem+".1gram")
        
        print("\tLoading %s.1gram_context" %file_stem, file=sys.stderr)
        unigram_context = read_frequency(file_stem+".1gram_context")
        
        uni_N = unigrams['#Total'] # unigram 빈도 합
        
        t_scores = calc_tscore(input_file, unigrams, unigram_context, uni_N, CUTOFF)
        
        print_tscore(file_stem+".tscore", t_scores)

