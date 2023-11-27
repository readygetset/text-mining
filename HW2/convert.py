from collections import defaultdict

convert = defaultdict(str)
with open ('./trn.txt','r', encoding='UTF-8') as trn_file:
    for line in trn_file.readlines():
        if(len(line.split())==2):
            convert[line.split()[0]]=line.split()[1]

test_file = open('./sample57.txt','r', encoding='UTF-8')
result_file = open('result.txt','w',encoding='UTF-8')
cnt=0
write_list=[]
for line in test_file.readlines():
    line = line.strip()
    if line in convert.keys():
        result_file.writelines(line+'\t'+convert[line]+'\n')
        cnt+=1
    elif line == '':
        result_file.writelines('\n')
        cnt+=1
    else:
        result_file.writelines(line+'\n')
        cnt+=1
        write_list.append(cnt)
print(write_list)
print(len(write_list))