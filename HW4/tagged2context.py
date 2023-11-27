#!/usr/bin/env python3
#coding: utf-8

import sys
import get_morphs_tags as mf

###############################################################################
# 색인어 추출
def get_index_terms(mt_list):
    context_tag = ['NNG','NNP','NR','NNB','SL','SH','SN']
    indiv_context_tag = ['NNG','NNP','SH','SL']
    
    current_context_word = []
    total_context_word = []
    for m,t in mt_list:
        if t in context_tag:
            current_context_word.append((m,t))
        else:
            if len(current_context_word) > 0:
                if len(current_context_word) > 1:
                    total_word = ''
                    for context_m, context_t in current_context_word:
                        if context_t != 'SL' and context_t in indiv_context_tag:
                            total_context_word.append(context_m)
                        total_word += context_m
                    total_context_word.append(total_word)
                    current_context_word = []
                else:
                    indiv_context_m, indiv_context_t = current_context_word[0]
                    if indiv_context_t in indiv_context_tag:
                        total_context_word.append(indiv_context_m)
                    current_context_word = []
    if len(current_context_word) > 0:
        if len(current_context_word) > 1:
            total_word = ''
            for context_m, context_t in current_context_word:
                if context_t != 'SL' and context_t in indiv_context_tag:
                    total_context_word.append(context_m)
                total_word += context_m
            total_context_word.append(total_word)
            current_context_word = []
        else:
            indiv_context_m, indiv_context_t = current_context_word[0]
            if indiv_context_t in indiv_context_tag:
                total_context_word.append(indiv_context_m)
            current_context_word = []
    return total_context_word
###############################################################################
# Converting POS tagged corpus to a context file
def tagged2context( input_file, output_file):
    try:
        fin = open( input_file, "r")
    except:
        print( "File open error: ", input_file, file=sys.stderr)
        sys.exit()

    try:
        fout = open( output_file, "w")
    except:
        print( "File open error: ", output_file, file=sys.stderr)
        sys.exit()

    for line in fin.readlines():
    
        # 빈 라인 (문장 경계)
        if line[0] == '\n':
            print("", file=fout)
            continue

        try:
            ej, tagged = line.split(sep='\t')
        except:
            print(line, file=sys.stderr)
            continue

        # 형태소, 품사 추출
        # return : list of tuples
        result = mf.get_morphs_tags(tagged.rstrip())
        
        # 색인어 추출
        # return : list
        terms = get_index_terms(result) 
        
        # 색인어 출력
        for term in terms:
            print(term, end=" ", file=fout)
        
    fin.close()
    fout.close()
    
###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "file(s)", file=sys.stderr)
        sys.exit()

    for input_file in sys.argv[1:]:
        output_file = input_file + ".context"
        print( 'processing %s -> %s' %(input_file, output_file), file=sys.stderr)
        
        # 형태소 분석 파일 -> 문맥 파일
        tagged2context( input_file, output_file)
