import nltk
read_file=open('sample_biology_notes.txt','r')
import nltk.data
import pandas as pd
import statistics





sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

def clean_text(file):

    clean_list=[]
    for line in file:
        clean_list.append(line.strip())

    clean_text1=' '.join(clean_list)
    #strip away nonascii
    for each in clean_text1:
        if not each.isascii():
            clean_text2 = clean_text1.replace(each, '')
    # unwanted character
    unw_char=["-",'\n','\t','\xa0']
    for each in clean_text2:
        if each in unw_char:
            clean_text3 = clean_text2.replace(each, '')
    return clean_text3

clean_text_read=clean_text(read_file)
#clean_text_read

def clean_word(text):
    unw_char = ["-", '\n', '\t', '\xa0']
    for each in text:
        if each.isalnum()==False:
            clean=text.replace(each,' ')
            return clean
def sort_maxword(freqdict):
    freq_tup=list(freqdict.items())
    count_list=[]
    for key,value in freq_tup:
        count_list.append(value)
    freq_tup.sort(key= lambda x: x[1],reverse=True)
    mean_count=statistics.mean(count_list)
    sd=statistics.stdev(count_list)

    max_word_list=[]
    for key,value in freq_tup:
        if value >= (mean_count+1.5*sd):
            max_word_list.append(key)
    print(max_word_list)
    return max_word_list


    print(mean_count)
    print(sd)











import nltk.tokenize.punkt as punk

punk_cl=punk.PunktSentenceTokenizer()
sent_break=punk_cl.sentences_from_text(clean_text_read)

for sentence in sent_break:
    ind =sent_break.index(sentence)
    clean = clean_word(sentence)
    del sent_break[ind]
    sent_break.insert(ind,clean)





word_read=open('combined_biology_wordlist.txt','r')
bio_word=word_read.readlines()
clean_bio_word=[]
for i in bio_word:
    new=i.strip()
    clean_bio_word.append(new)



df=pd.DataFrame(sent_break,columns=['sentence'])
maxword_list=[]
print(df)

import nltk
from nltk.corpus import stopwords
non_meaning=stopwords.words('english')

for each in sent_break:
    words_li=each.split()
    freq_dict={}
    for i in words_li:
        if i.lower() not in non_meaning:
            word=i.lower()
            if  word not in freq_dict:
                freq_dict[word]=1
            else:
                freq_dict[word]+=1
            for each in freq_dict:
                if each in clean_bio_word:
                    val=freq_dict[each]
                    freq_dict[each]=val*1.3
                else:
                    val = freq_dict[each]
                    freq_dict[each] = val * 0.98
    maxword=sort_maxword(freq_dict)
    maxword_list.append(maxword)

df['Topic']= maxword_list



print(df)










