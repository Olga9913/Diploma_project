import re
import spacy

num_lines = 0
num_words = 0
num_chars = 0



# load data
with open('D://Diploma//Parameters//text.txt', encoding='utf8') as f:
    for line in f:
        num_lines += 1 # кол-во строк

with open('D://Diploma//Parameters//text.txt', encoding='utf8') as f:
    text = f.read()
    f.close()

list_of_sentences = []
nlp = spacy.load("de_core_news_sm")
doc = nlp(text)
assert doc.has_annotation("SENT_START")
for sent in doc.sents:
    result_sentences=sent.text


    delite_punctuation = [re.sub(r'[^\-\&\w\s]','',w) for w in result_sentences]
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
print(new_list)


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


wordcounts=[]
for sentence in new_unpack_list_clear:
    words = sentence.split(' ')
    wordcounts.append(len(words))
print("кол-во слов:",sum(wordcounts))
    #m_words += len(words)
    #num_chars += len(line) # нужно отфильтровать от лишних знаков и символов перед подсчитыванием символов


#print('Number of lines: ',num_lines,' Number of words: ', num_words,' Number of chars: ', num_chars)
print('Number of lines: ',num_lines)

for sentence in new_unpack_list_clear: # подсчет кол-ва символов в тексте. Нужно ли считать дефисы
    pattern = re.compile(r'\s+')
    element = re.sub(pattern, '', sentence)
    for char in element:
        num_chars += 1

"""        join_words = ' '.join(sentence)
        for char in sentence:
            num_chars += 1"""


print("число символов",num_chars)