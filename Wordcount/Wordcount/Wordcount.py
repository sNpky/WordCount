import re
def My_lines_count(file_name):
    #用来统计文本文件里面的行数
    #file_name=input("请输入你希望操作的文件名需要加.txt':")
    line_num=0
    with open(file_name,'rb') as f:
        lines=f.readlines()
        for each_line in lines:
            if each_line!='\n':
                line_num+=1
            
    
    f.close()    
    return "lines:"+str(line_num)    


def My_chars_count(file_name):
    #用来统计文本文件里面的字符数量
    
    with open(file_name,'rb') as f:
        chars=f.read()
    f.close()    
    return 'chars:'+str(len(chars))


def My_words_count(file_name):
    #用来统计文本文件里面的单词数量规定4个字母以上的单词
    words=[]
    word=0
    with open(file_name,'r') as f:
        lines=f.readlines()
        for N in range(0,len(lines)):
            words.extend(re.findall(r'[(a-z|A-Z)]{4,}',lines[N]))
    word+=len(words)   
    f.close()    
    return "words:"+str(word)

def My_dgtwords_count(file_name):
    #用来统计文本文件里面的指定单词长度词组词的数量，这里是3个长度的词组
    words=[]
    word=0
    with open(file_name,'r') as f:
        lines=f.readlines()
        for N in range(0,len(lines)):
            words.extend(re.findall(r'[(a-z|A-Z)]{3}',lines[N]))
    word+=len(words)   
    f.close()    
    return "designatewords:"+str(word)

def word_count(file_name):
    #记录文本中单词出现的频率，并且按照出现频率打印出来
    #words列表存放有重复的单词
    words=[]
    with open(file_name,'r') as f:
        lines=f.readlines()
        for N in range(0,len(lines)):
            words.extend(re.findall(r'[(a-z|A-Z)(a-z|A-Z)(a-z|A-Z)(a-z|A-Z)]{1,}',lines[N]))
    #利用了python字典的特性dict{key:value},字典里面映射关系不会出现键key的重复
    #创建一个字典存放单词和其频率
    wokey={}
    #用有重复单词的列表来给字典赋值，而在字典中就不会用重复了但是key对应的value的值没有变的
    wokey=wokey.fromkeys(words)
    #新定义一个单词列表来存放无重复的单词
    wordlist=list(wokey.keys())
    for i in wordlist:
        #得到无重复的词频
        wokey[i]=words.count(i)
    wokey_1={}
    wokey_1=sorted(wokey.items(),key=lambda p:p[1],reverse=1)
    i=0
    for x,y in wokey_1:
        if i<10:
            print('%s’s frequence: %d'%(x,y))
            i+=1
            continue
        else:
             break
    f.close()    

    
def My_cmd():
    command,file_name=input("Please input command").split()
    if command=='-i':
        #记录字符的数量
        print(My_chars_count(file_name))
    if command=='-d':
        #记录指定长度词组的数量
        print(My_dgtwords_count(file_name))
        
    if command=='-o':
        #记录符合条件单词的数量
         print(My_words_count(file_name))
    
    if command=='-u':
        #记录有效行数
        print(My_lines_count(file_name))
    if command=='-e':
        #记录词频
        print(word_count(file_name))
    if command=='-i-o':
        #记录字符的数量,记录符合条件单词的数量
        print(My_chars_count(file_name))
        print(My_words_count(file_name))
    if command=='-i-u':
        #记录字符的数量,记录有效行数
        print(My_chars_count(file_name))
        print(My_lines_count(file_name))
    if command=='-i-e':
        #记录字符的数量,#记录词频
        print(My_chars_count(file_name))
        print(word_count(file_name))
    if command=='-i-o-u':
        #记录字符的数量,记录符合条件单词的数量,记录有效行数
        print(My_chars_count(file_name))
        print(My_words_count(file_name))
        print(My_lines_count(file_name))
    if command=='-i-o-u-e':
        #记录字符的数量记录符合条件单词的数量,记录有效行数，记录词频
        print(My_chars_count(file_name))
        print(My_words_count(file_name))
        print(My_lines_count(file_name))
        print(word_count(file_name))
    if command=='-i-o-u-e-d':
        #记录字符的数量记录符合条件单词的数量,记录有效行数，记录词频，附加功能
        print(My_chars_count(file_name))
        print(My_words_count(file_name))
        print(My_lines_count(file_name))
        print(word_count(file_name))
        print(My_dgtwords_count(file_name))
    if command=='-i-o-e':
        #记录字符的数量记录符合条件单词的数量,记录词频
        print(My_chars_count(file_name))
        print(My_words_count(file_name))
        print(word_count(file_name))
    if command=='-o-u':
        #记录符合条件单词的数量,有效行数
        print(My_words_count(file_name))
        print(My_lines_count(file_name))
    if command=='-o-e':
        #记录符合条件单词的数量和词频
        print(My_chars_count(file_name))
    if command=='-u-e':
        #记录有效行数和词频
        print(My_lines_count(file_name))
        print(word_count(file_name))

My_cmd()
