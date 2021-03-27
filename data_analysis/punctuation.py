import string

text="""
Pflegepraktikum.
Schmerzen, Weinen, Lachen.
Klinikclowns, Bärchen-Pflaster und die Welt ist wieder in Ordnung. 
Halbzeit im Pflegepraktikum auf der Kinderchirurgischen Station.
Hypospadie, Appendizitis, Schädelprellung, Unteramfraktur, Unteramfraktur und natürlich die Unteramfraktur? Dabei nimmt das Trampolin eine Hauptrolle ein. Spannend. Wir haben wirklich unterschiedliche chirurgische Eingriffe aber die Unteramfraktur kommt tatsächlich sehr oft vor. Trotzdem ist es super abwechslungsreich. Die Gespräche mit den Eltern können anstrengend sein, müssen sie aber nicht & die Arbeit mit den Kindern ist etwas ganz besonderes. Egal wie schlecht es den Kindern geht, ein Lächeln bekommt man mindestens 1x von jedem Kind geschenkt.
Bei uns liegen Kinder von wenigen Wochen alt bis 18 Jahre. Alles hat seinen Reiz. Das Ablenken der ganz kleinen, die Bärchenpflaster bei den Kleinkindern und die Gespräche mit den Jugendlichen.
Pädiatrie ist toll. Ich bleibe dabei.
Klingt toll😍 Könntest du dir vorstellen später in diese Richtung zu gehen?
absolut! Einer meiner Hauptgründe, weswegen ich Medizin studieren wollte/will. ☺️
dann wünsche ich weiterhin ganz viel Spaß und Erfolg. 🍀😊
Klingt super spannend. Pädiatrie ist neben der Gyn meine zweite Wahl! 😍 Ich wünsche dir noch ganz viel Spaß
danke! :) Gyn/ Geburtshilfe ist bestimmt auch super interessant
Sehr interessant, obwohl ich pädiatrie auch immer wieder sehr schwierig im Sinne von belastend finde, weil die Kinder teilweise so „schutzlos“ sind 🙈✨
ja das stimmt !
    """
text_split=text.split()
print(text_split)
# Storing the sets of punctuation in variable result
result = string.punctuation
# Printing the punctuation values
print(result)
all_punctuation_from_text=[]
list_of_punctuation=list(result)
for i in list_of_punctuation:
    for el in text_split:
        if i in el:
            all_punctuation_from_text.append(i)
print(all_punctuation_from_text)

# проверить тест на пунктуацию
# проходим по очереди по списку; если элемент есть в тексте, то прибавляем в переменную элемента

from collections import Counter

#array = ["Bob", "Alex", "Bob", "John"]

c = Counter(all_punctuation_from_text)

print(c) # статистика употребления пунктуации; НЕ УЧИТЫВАЮТСЯ СМАЙЛИКИ ИЗ ПУНКТУАЦИИ - " :) "
# позже выделить знаки смайликов из пункт-и и исключить их!!!!!!
