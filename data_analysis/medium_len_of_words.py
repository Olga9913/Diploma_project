import re
with open('D://Diploma//Parameters//text.txt', encoding='utf8') as f:
    text = f.read()
def avg_word_len(text):
    text = text.replace("\n"," ")
    words = text.split(' ') # presuming words split by ' '. be watchful about '.' and '?' below
    words_new = [re.sub(r'[^\-\w\s]','',w) for w in words] # без любых других символов и знаков пунктуации
    #words_new = [re.sub(r'\&|\?|\.|\!|\,','',w) for w in words]# re sub '[^\w\s]' to remove punctuations first  # убраны только определенные знаки
    for i in words_new:
        if i == '':
            words_new.remove('')
        if i == ' ':
            words_new.remove(' ')
    print("список слов",words_new)
    print("кол-во слов",len(words_new))
    return sum(len(w) for w in words_new)/float(len(words_new)) # then calculate the avg, dont forget to render answer as a float

if __name__ == "__main__":
    print (avg_word_len(text))

"""
сделать удаление пунктуации по конкретным знакам,чтобы не потерять симвоы
все n убрать и заменить на пробелы
проверить чтоб дефисы не удалялись
чтобы 1x цифры остались
"""