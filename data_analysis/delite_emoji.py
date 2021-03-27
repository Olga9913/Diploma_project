import re

data = """
Klingt toll😍 
absolut! Einer meiner Hauptgründe, weswegen ich Medizin studieren wollte/will. ☺️
dann wünsche ich weiterhin ganz viel Spaß und Erfolg. 🍀😊
Klingt super spannend. Pädiatrie ist neben der Gyn meine zweite Wahl! 😍 
Klingt nach einer sehr sehr tollen Erfahrung 😍
Die Pädiatrie ist einfach wundervoll 🥰
1. Semester ✅🥳
Dazu folgt in nächster Zeit aber nochmal ein ausführlicher Post. 👶🏻
Ersti in Zeiten von Corona 🦠
"""
def remove_emojis(data):

    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)

    return re.sub(emoj, '', data)

print(remove_emojis(data))
