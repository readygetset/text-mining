import sys
import pickle
from collections import defaultdict
'''
1. 각 입력 파일의 각 단어에 대해 개별 문자들로 이루어진 토큰 튜플, 빈도 쌍을 corpus 딕셔너리에 저장 (제공된 main 함수 코드에 구현되어 있음)
2. 인접 토큰 쌍 빈도 계산
3. 가장 높은 빈도를 가진 토큰 쌍을 vocab 리스트에 저장하고 corpus에 반영
   * 변화가 없거나 가장 높은 빈도를 가진 토큰 쌍의 빈도가 1이면 학습을 종료하도록 해야 함 *
'''

def bpe_learn(corpus):
    iteration = 0
    vocab = []

    while True:

        corpus_dict = defaultdict(int)
        for token, frequency in corpus.items(): 
            for i in range(len(token) - 1):
                pair = (token[i], token[i+1])
                corpus_dict[pair] += frequency # 토큰 튜플과 그 빈도 쌍을 딕셔너리에 저장 (2번)

        if len(corpus_dict) == 0:
            break

        most_common = max(corpus_dict, key = corpus_dict.get)
        vocab.append(most_common) # 딕셔너리에서 가장 높은 빈도를 가진 토큰 쌍을 vocab 리스트에 저장 (3-1번)
        print("iteration: %d (max = %d, %s)"%(iteration, corpus_dict[most_common], most_common[0] + most_common[1])) # 반복 횟수 및 가장 높은 빈도를 가진 토큰 쌍과 그 빈도 출력

        if corpus_dict[most_common] == 1: break # 가장 높은 빈도를 가진 토큰 쌍의 빈도가 1이면 학습 종료

        corpus_update = defaultdict(int)
        for token, frequency in corpus.items():
            i = 0
            token_update = []
            while i < len(token) -1:
                if(token[i], token[i+1]) == most_common: #가장 높은 빈도를 가진 토큰 쌍을 corpus에 반영 (3-2번)
                    token_update.append(token[i] + token[i+1])
                    i += 2
                else:
                    token_update.append(token[i])
                    i += 1
            if i == len(token) - 1:
                token_update.append(token[i])

            corpus_update[tuple(token_update)] += frequency
        
        if corpus == corpus_update: break # 변화가 없으면 학습 종료
        
        corpus = corpus_update
        iteration += 1
            
    return vocab


if __name__ == "__main__":

    # 입력 파일 없을 경우, 오류 메세지 출력 후 스크립트 종료
    if len(sys.argv) < 2: 
        print("%s file(s)"% sys.argv[0], file=sys.stderr)
        sys.exit()

    corpus = defaultdict(int) # 각 단어의 토큰 및 빈도를 저장하는 튜플
    vocab = [] # 가장 높은 빈도를 가진 토큰 쌍을 저장하는 리스트

    for file in sys.argv[1:]: # 전달된 각 파일에 대해 for loop
        print("processing %s" %file, file=sys.stderr) # 현재 처리 중인 파일을 표시하는 메세지 출력
        with open(file) as fin: # 현재 파일 open
            for line in fin: # 파일 내의 각 line에 대해 for loop
                for w in line.split(): # 공백 기준으로 단어 분리 후 각 단어에 대해 for loop
                    corpus[tuple(w+"_")] += 1 # 단어의 개별 문자들로 이루어진 토큰 튜플을 key로, 단어의 빈도를 value로 하는 딕셔너리


    print("corpus size = %d tokens" %len(corpus), file=sys.stderr) # corpus에 저장된 토큰의 총 개수 출력

    vocab = bpe_learn(corpus)
    with open("vocab.pickle", "wb") as fout:
        pickle.dump(vocab, fout)

    print("bpe_learn successfully completed!")