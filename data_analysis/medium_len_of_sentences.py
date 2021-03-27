import re
#import nltk
import spacy

list_of_sentences = []
"""nltk.download('punkt')
from nltk import sent_tokenize"""
# load data
with open('D://Diploma//Parameters//text.txt', encoding='utf8') as f:
    text = f.read()
    f.close()

nlp = spacy.load("de_core_news_sm")
doc = nlp(text)
assert doc.has_annotation("SENT_START")
for sent in doc.sents:
    result_sentences=sent.text
    #print(result_sentences)# разделили по предложениям
   # split into sentences
    """sentences = sent_tokenize(full_text)
    print(sentences)"""

    delite_punctuation = [re.sub(r'[^\-\&\w\s]','',w) for w in result_sentences]
    #print(delite_punctuation)
    test_list="".join(delite_punctuation)
    list_of_sentences.append(test_list)
print(list_of_sentences)


new_list=[]
for sentence in list_of_sentences: # для каждого элемента (предложения) в списке
        if '\n' in sentence: # если в предложении есть такой знак, то ...
            words_split = sentence.split('\n') # заводим переменную, в которую вкладываем: предложение разделенное по \n
            new_list.append(words_split)
        else:
            new_list.append(sentence)
            #list_of_sentences.insert(n, words_split)
print(new_list)
            # добавить новые предложения на место старых
            #delite_punctuation.insert(n, words_split)
            # добавить words как новый элемент в список; list.insert(i, x)

from collections import Iterable
def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:
             yield item

new_unpack_list=list(flatten(new_list))
print('result',new_unpack_list)



new_unpack_list_clear=[i for i in new_unpack_list if i != '']
print("new_unpack_list_clear",new_unpack_list_clear)
"""for element in new_unpack_list:
    if element=='':
        new_unpack_list.remove(element)"""




wordcounts=[]
for sentence in new_unpack_list_clear:
    words = sentence.split(' ')
    wordcounts.append(len(words))
print(wordcounts)
average_wordcount = sum(wordcounts)/len(wordcounts)
print(average_wordcount)
"""import re
wordcounts = []
with open('D://Diploma//Parameters//text.txt', encoding='utf8') as f:
    text = f.read()
    text_delete_punctuation=re.split(r'[?+|.+|!+|\n]',text)
    text_delete_punctuation=list(filter(None, text_delete_punctuation))
    for i in  text_delete_punctuation:
        i.lstrip(' ')
        i.rstrip(' ')
        if i == ' ':
            text_delete_punctuation.remove(' ')


    print(text_delete_punctuation)
    for sentence in text_delete_punctuation:
        words = sentence.split(' ')
        wordcounts.append(len(words))
print(wordcounts)
average_wordcount = sum(wordcounts)/len(wordcounts)
print(average_wordcount)"""
"""
s = ['www.abc.com/1/2/3', 'www.xyz.com/3/4/5', 'www.try.com/6/7/5']
result=[re.sub('/*','',i) for i in s]
1) почему в конце остается пробел в списке?
2) 
"""





