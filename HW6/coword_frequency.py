#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict
from itertools import combinations

###############################################################################
def get_word_freq(filename):

    fin = open(filename, 'r')
    
    word_freq = defaultdict(int)
    total_unigram_count = 0

    for line in fin.readlines():
        words = set(line.split())
        for word in words:
            total_unigram_count += 1
            if (word in word_freq):
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    return word_freq, total_unigram_count

###############################################################################
def print_word_freq(filename, word_freq):

    fout = open(filename, 'w')
    word_freq = dict(sorted(word_freq.items()))

    if 'total_unigram_count' in word_freq:
        print('#Total\t%d'%(word_freq['total_unigram_count']), file=fout)
        del word_freq['total_unigram_count']

    for word, freq in word_freq.items():
        print(word,'\t', freq, file=fout)

###############################################################################
def get_coword_freq(filename):

    fin = open(filename, 'r')

    coword_freq = defaultdict(int)
    word_context_size = defaultdict(int)

    word_freq, total_unigram_count = get_word_freq(filename)
    word_freq['total_unigram_count'] = total_unigram_count

    for line in fin.readlines():
        words = set(line.split())
        word_comb = combinations(words, 2)
        
        for word in words:
            if (word in word_context_size):
                word_context_size[word] += len(words)
            else:
                word_context_size[word] = len(words)

        for w1, w2 in word_comb:
            if w1 < w2:
                word_tuple = (w1, w2)
            else:
                word_tuple = (w2, w1)
            if (word_tuple in coword_freq):
                coword_freq[word_tuple] += 1
            else:
                coword_freq[word_tuple] = 1
                
    return word_freq, coword_freq, word_context_size

###############################################################################
def print_coword_freq(filename, coword_freq):

    fout = open(filename, 'w')

    coword_freq = dict(sorted(coword_freq.items()))

    for word_tuple, freq in coword_freq.items():
        w1, w2 = word_tuple
        print('%s\t%s\t%d'%(w1, w2, freq), file=fout)

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    for input_file in sys.argv[1:]:
        
        print( 'processing %s' %input_file, file=sys.stderr)
        
        file_stem = input_file
        pos = input_file.find(".")
        if pos != -1:
            file_stem = input_file[:pos] # ex) "2017.tag.context" -> "2017"
        
        # 1gram, 2gram, 1gram context 빈도를 알아냄
        word_freq, coword_freq, word_context_size = get_coword_freq(input_file)

        # unigram 출력
        print_word_freq(file_stem+".1gram", word_freq)
        
        # bigram(co-word) 출력
        print_coword_freq(file_stem+".2gram", coword_freq)

        # unigram context 출력
        print_word_freq(file_stem+".1gram_context", word_context_size)
