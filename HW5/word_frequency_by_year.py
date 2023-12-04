#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

def word_count(file_count, filename, word_freq):

    with open(filename, "r", encoding='utf-8') as fin:
        for word in fin.read().split():
            if word in word_freq:
                word_freq[word][file_count]+=1
            else:
                empty_list = []
                for i in range(20):
                    empty_list.append(0)
                word_freq[word] = empty_list
                word_freq[word][file_count]+=1

    return word_freq

if __name__ =="__main__":
    if len(sys.argv) < 2:
        print("[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    file_count = 0
    word_freq = defaultdict(list)

    for input_file in sys.argv[1:]:
        print('processing %s' %input_file, file=sys.stderr)
        word_freq = word_count(file_count, input_file, word_freq)
        file_count+=1

    for word, freqList in sorted(word_freq.items()):
        #print("%s\t%s"%(word, freqList))
        print(word+'\t'+str(freqList))