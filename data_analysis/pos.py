import spacy

nlp = spacy.load('de_core_news_sm')
with open('D://Diploma//Parameters//text.txt', encoding='utf8') as f:
    text = f.read()
    doc = nlp(text)
spacy_text=' '.join('{word}/{tag}'.format(word=t.orth_, tag=t.pos_) for t in doc)
key_dict = {}
lst_space = spacy_text.split(" ")
for i in lst_space:
    lst_slash = i.split("/")
    key=lst_slash[0]
    value = lst_slash[1]
    key_dict[key] = value

print(key_dict)

# Open class words: ADJ, ADV, INTJ, NOUN, PROPN, VERB
result_dict = {'NOUN' : 0, 'ADJ' : 0,'ADV' :0, 'INTJ' : 0, 'PROPN':0, 'VERB':0}
for key, value in key_dict.items():
    if value =="NOUN":
        result_dict['NOUN'] +=1
    elif value =="ADJ":
        result_dict['ADJ'] +=1
    elif value == "ADV":
        result_dict['ADV'] += 1
    elif value == "INTJ":
        result_dict['INTJ'] += 1
    elif value == "PROPN":
        result_dict['PROPN'] += 1
    elif value == "VERB":
        result_dict['VERB'] += 1

print(result_dict)

# Closed class words: ADP, AUX, CCONJ, DET, NUM, PART, PRON, SCONJ
result_dict2 = {'ADP' : 0, 'AUX' : 0,'CCONJ' :0, 'DET' : 0, 'NUM':0, 'PART':0, 'PRON':0, 'SCONJ':0}
for key, value in key_dict.items():
    if value =="ADP":
        result_dict2['ADP'] +=1
    elif value =="AUX":
        result_dict2['AUX'] +=1
    elif value == "CCONJ":
        result_dict2['CCONJ'] += 1
    elif value == "DET":
        result_dict2['DET'] += 1
    elif value == "NUM":
        result_dict2['NUM'] += 1
    elif value == "PART":
        result_dict2['PART'] += 1
    elif value == "PRON":
        result_dict2['PRON'] += 1
    elif value == "SCONJ":
        result_dict2['SCONJ'] += 1

print(result_dict2)

"""
    line=line.replace('\n', '')
    key_dict={}
    substr_list=line.split(",")
    for substr in substr_list:
        newlist=substr.split('=')
        key=newlist[0]
        value=newlist[1]
        key_dict[key]=value
    print(key_dict)
"""
"""with open("text_write.txt", "w") as write_in_file:
    write_in_file.write(doc)"""

"""сделать обращение к файлу
создать список из данных и подсчитать в нем частей речи. Вывести в таблицу.
Open class words: ADJ, ADV, INTJ, NOUN, PROPN, VERB
Closed class words: ADP, AUX, CCONJ, DET, NUM, PART, PRON, SCONJ
Other: PUNCT; символы и просто набор букв не распознает.

lst_space = doc.split()
lst_slash = doc.split("/")
print(lst_slash)
sentences = {}
for element in doc:
    key = element.find('NAME').text
    value = element.find('ROOM').text
    dict_from_file[key] = value
"""
