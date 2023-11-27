import sys
import pickle

'''
1. 각 입력 파일의 각 단어에 대해, 문자 단위로 분해
2. vocab 리스트의 각 토큰 쌍이 1의 결과에서 발견되는지 검사. 발견되는 토큰 쌍을 결합 후 치환.
   * 전체 문자열이 하나의 토큰이 되면 loop를 종료하도록 해야 함 *
3. 2의 결과에서 '_' 제거
4. 3의 결과를 '+'로 구분하여 문자열로 결합
5. 출력 파일에 저장
'''

def tokenizer(tokens, vocab):
    while True:
        if len(tokens) > 1:
            i = 0
            change = False
            while i < len(tokens) - 1:
                pair = tokens[i] + tokens[i+1] 
                if pair in vocab: # vocab 리스트의 각 토큰 쌍에서 pair가 발견되는지 검사 (2-1번)
                    tokens[i] = pair # 발견되는 토큰 쌍을 치환 (2-2번)
                    tokens.pop(i+1)
                    change=True
                i += 1
        else: break
        if(change==False): break
    return tokens
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("%s file" % sys.argv[0], file=sys.stderr)
        sys.exit()

    vocab = []

    with open('./vocab_prof.pickle', 'rb') as fin:
        vocab = pickle.load(fin)
    vocab = [item for tpl in vocab for item in tpl]

    for file in sys.argv[1:]:
        print("processing %s -> %s" % (file, file + ".bpe"), file=sys.stderr)
        fin = open(file, "rt")
        fout = open(file + ".bpe", "wt")

        for line in fin:
            bpe_segmented_token = []
            for w in line.split():
                original_token = list(w+'_')
                bpe_segmented_token = tokenizer(original_token, vocab)
                bpe_segmented_token = [token.replace('_', '') for token in bpe_segmented_token]
                if '' in bpe_segmented_token: bpe_segmented_token.remove('')
                bpe_segmented_token = '+'.join(bpe_segmented_token)
                fout.write(w + '\t' + bpe_segmented_token + '\n')

        fin.close()
        fout.close()
