#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pickle
import math # sqrt

###############################################################################
def cosine_similarity(t_vector, c_vector):

    numerator = 0
    denominator_t = 0
    denominator_c = 0

    for coword, t_score in t_vector.items():
        denominator_t += t_score ** 2
        if coword in c_vector:
            numerator += t_score * c_vector[coword]

    for coword, t_score in c_vector.items():
        denominator_c += t_score ** 2

    denominator_t = math.sqrt(denominator_t)
    denominator_c = math.sqrt(denominator_c)

    return numerator/(denominator_t*denominator_c)

###############################################################################
def most_similar_words(word_vectors, target, topN=10):

    result = {}
    for coword in word_vectors[target].keys():
        if coword != target and coword not in target:
            cos_sim = cosine_similarity(word_vectors[target], word_vectors[coword])
            if cos_sim > 0.001:
                result[coword] = cos_sim
        for co_coword in word_vectors[coword].keys():
            if co_coword != target and co_coword not in target:
                cos_sim = cosine_similarity(word_vectors[target], word_vectors[co_coword])
                if cos_sim > 0.001:
                    result[co_coword] = cos_sim

    return sorted(result.items(), key=lambda x: x[1], reverse=True)[:topN]

###############################################################################
def print_words(words):
    for word, score in words:
        print("%s\t%.3f" %(word, score))

###############################################################################
def search_most_similar_words(word_vectors, topN=10):

    print('\n검색할 단어를 입력하세요(type "^D" to exit): ', file=sys.stderr)
    query = sys.stdin.readline().rstrip()

    while query:
        # result : list of tuples, sorted by cosine similarity
        result = most_similar_words(word_vectors, query, topN)
        
        if result:
            print_words(result)
        else:
            print('\n결과가 없습니다.')

        print('\n검색할 단어를 입력하세요(type "^D" to exit): ', file=sys.stderr)
        query = sys.stdin.readline().rstrip()
    
###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print( "[Usage]", sys.argv[0], "in-file(pickle)", file=sys.stderr)
        sys.exit()

    topN = 30
    
    with open(sys.argv[1],"rb") as fin:
        word_vectors = pickle.load(fin)
    
    search_most_similar_words(word_vectors, topN)