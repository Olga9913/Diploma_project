"""
убрать стоп-слова из текста
подсчитать частотность
"""
text1="""
Klingt super spannend. Pädiatrie ist neben der Gyn meine zweite Wahl! 😍 Ich wünsche dir noch ganz viel Spaß
danke! :) Gyn/ Geburtshilfe ist bestimmt auch super interessant
Sehr interessant, obwohl ich pädiatrie auch immer wieder sehr schwierig im Sinne von belastend finde, weil die Kinder teilweise so „schutzlos“ sind 🙈✨
ja das stimmt !
Klingt nach einer sehr sehr tollen Erfahrung 😍
Die Pädiatrie ist einfach wundervoll 🥰 Ich werde wohl auch als Ärztin später nicht von der Pädiatrie wegkommen🙈
ja so toll
1. Semester ✅🥳
Nach langer Zeit melde ich mich auch mal wieder zu Wort.
Das erste Semester ist geschafft. Vor einer Woche war meine Klausur und die vorläufigen Ergebnisse haben wir auch relativ schnell bekommen. Bestanden 💪🏻☺️. Die erste Klausur war tatsächlich kein Hexenwerk, an der Charité schreibt man im 1. Semester eine MC Klausur, 60 Fragen. Davon waren dieses Jahr tatsächlich die Hälfte Altfragen, was wirklich großzügig war. Dementsprechend lief die Klausur auch recht gut. Ich glaube das schwierigste am Medizinstudium ist die Zulassung zu bekommen & dafür bin ich immer noch so unglaublich dankbar. 🙏🏻😍Jetzt bin ich aber auch froh, dass das erste Semester geschafft ist - oder auch das Corona Semester.
Auch wenn im 2. Semester vermutlich auch wieder viel online stattfinden wird, hoffe ich, dass die praktischen Teile umgesetzt werden.
Ansonsten bin ich seit Montag in der Kinderklinik im Pflegepraktikum. 30 Tage bin ich hier und ich weiß jetzt schon, dass ich die letzten 30 Tage auch hier verbringen werde. Es ist einfach so viel besser, als das erste Praktikum. Die Arbeit mit den Kindern macht super viel Spaß.
Dazu folgt in nächster Zeit aber nochmal ein ausführlicher Post. 👶🏻
Ersti in Zeiten von Corona 🦠
"""
# образуем список из слов
import re
import nltk
nltk.download('punkt')
from nltk import sent_tokenize
# load data
with open('D://Diploma//Parameters//medizin.txt', encoding='utf8') as f:
    text = f.read()
    f.close()

# split into sentences
    sentences = sent_tokenize(text)


# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)


# remove all tokens that are not alphabetic
words_new = [re.sub(r'[^\-\w\s]','',w) for w in tokens] # без любых других символов и знаков пунктуации
#words_new = [re.sub(r'\&|\?|\.|\!|\,','',w) for w in tokens] # убраны только определенные знаки
for i in words_new:
    if i == '':
        words_new.remove('')
    if i == ' ':
        words_new.remove(' ')
print("список слов:",words_new)
#print(sum(len(w) for w in words_new)/float(len(words_new)))

# удалим стоп-слова
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords_ger = stopwords.words('german')

#final_wordlist =['Status', 'laufende', 'Projekte', 'bei', 'Stand', 'Ende', 'diese', 'Bei']
#stopwords_ger = stopwords.words('german')
#filtered_words = [w for w in final_wordlist if w not in stopwords_ger]
filtered_words = [w for w in words_new if w.lower() not in stopwords_ger]
print("список без стоп слов",filtered_words)

#
from collections import Counter

c = Counter(filtered_words)

print(c)

"""
1) Добавить стоп-слова свои, так как в тексте выделились вроде не все
2) убрать подсчитанные пробелы из списков результата
"""