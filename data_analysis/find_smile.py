import emoji

"""with open(r"D:\Diploma\Parameters\doing\english_emoji.txt", "r", encoding='utf8') as file:
    whole_list_emoji=file.read()"""
text="""
    🥈Kli😍 😍 Könntest du dir vorstellen später in diese Richtung zu gehen?
    absolut! Einer meiner Hauptgründe, weswegen ich Medizin studieren wollte/will. ☺️
    dann wünsche ich weiterhin ganz viel Spaß und Erfolg. 🍀😊
    Klingt super spannend. Pädiatrie ist neben der Gyn meine zweite Wahl! 😍 Ich wünsche dir noch ganz viel Spaß
    """
emoji_number=[]
split_text=text.split()
whole_list_emoji=emoji.UNICODE_EMOJI
emoji_en=whole_list_emoji.get('en')
emojis_df={}
for string in split_text:
    for each in string:
        #for val in emoji_en.values():
            for key_en in emoji_en.keys():
                if each==key_en:
                    emoji_number.append(each)
                    #emoji_en.get(key_en)
                    #for key, value in emoji_en.items():
                    emojis_df[key_en]=emoji_en.get(key_en)
print(emoji_number)
print(emojis_df)
# 1) как считывать только en
# 2) в значениях на испанском считывается бред
# story_count.get('двенадцать')

from collections import Counter


c = Counter(emoji_number)

print(c)