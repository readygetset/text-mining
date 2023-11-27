
result = open('result_form.txt','w',encoding='UTF-8')
cnt=0
with open ('./result.txt','r', encoding='UTF-8') as file:
    for line in file.readlines():
        if(len(line.split())==2):
            result.writelines(line.split()[0]+'\t'+line.split()[1]+'\n')
            cnt+=1
        else:
            result.writelines('\n')
            cnt+=1
print(cnt)