import re
import nltk
nltk.download('punkt')
from nltk import sent_tokenize
# load data
with open('D://Diploma//Parameters//text.txt', encoding='utf8') as f:
    text = f.read()
    f.close()

# split into sentences
    sentences = sent_tokenize(text)
#print(sentences)


# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
#print(tokens)

# remove all tokens that are not alphabetic

words_new = [re.sub(r'[^\-\w\s]','',w) for w in tokens] # без любых других символов и знаков пунктуации
#words_new = [re.sub(r'\&|\?|\.|\!|\,','',w) for w in tokens] # убраны только определенные знаки
for i in words_new:
    if i == '':
        words_new.remove('')
    if i == ' ':
        words_new.remove(' ')
print(words_new)
print(sum(len(w) for w in words_new)/float(len(words_new)))



