import re
from .helpers import alphabits, digits, char_replace, diacritics
uk = 'ـ'
punc = '٪.،؟'

def preprocess(c):
    special_char_dict = {}
    for r in char_replace:
        old, new = r[0], r[1]
        special_char_dict[old] = new
    
    map_table = c.maketrans(special_char_dict)
    c = c.translate(map_table)
    c = c.replace(uk, '')
    
    res = [ele if (ele in alphabits) or (ele in digits) or (ele in punc) else  ' ' for ele in c]
    c = ''.join(res)
    c = re.sub("["+digits+"]+", lambda ele: " " + ele[0] + " ", c)
    c = c.replace('\n', ' ')
    c = re.sub('\.+', '.', c)
    c = re.sub('،+', '،', c)
    c = re.sub('٪+', '٪', c)
    c = c.replace('، ،', '،').replace('٪ ٪', '٪')
    c = re.sub(' +', ' ', c)
    c = c.strip(' ،.')
    c = re.split('؟|\.', c)
    return c

# def preprocess(c):
#     c = basic_preprocessing(c)
#     c = c.replace('.', ' ')
#     c = re.sub(' +', ' ', c)
#     return c