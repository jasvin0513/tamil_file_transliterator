import re 

# Map Tamil characters to English. Credits to @saumikn on Github
consonants = {'க்க':'kk','ச்ச':'cc','ட்ட':'tt','த்த':'tt','ப்ப':'pp',
              'ங்க':'ng','ஞ்ச':'nj','ண்ட':'nd','ந்த':'nd','ம்ப':'mb',
              r'(^|\s)க':r'\1k',r'(^|\s)ச':r'\1c',r'(^|\s)ட':r'\1t',
              r'(^|\s)த':r'\1t',r'(^|\s)ப':r'\1p',
              'க':'g','ங':'ng','ச':'s','ஞ':'n','ட':'d','ண':'n',
              'த':'d','ந':'n','ப':'b','ம':'m','ய':'y','ர':'r',
              'ல':'l','வ':'v','ழ':'zh','ள':'l','ற':'r','ன':'n',
              'ஜ':'j','ஶ':'s','ஷ':'sh', 'ஸ':'s','ஹ':'h'}

vowels1 = {'ா':'aa','ி':'i','ீ':'ii','ு':'u','ூ':'uu','ெ':'e','ே':'ee',
           'ை':'ai','ொ':'o','ோ':'oo','ௌ':'au','்':'','':'a',}

vowels2 = {'அ':'a','ஆ':'aa','இ':'i','ஈ':'ii','உ':'u','ஊ':'uu',
           'எ':'e','ஏ':'ee','ஐ':'ai','ஒ':'o','ஓ':'oo','ஔ':'au',}

# Replace Tamil characters with their English counterpart
def transliterate(str):
    for c1, c2 in consonants.items():
        for v1, v2 in vowels1.items():
            str = re.sub(c1+v1, c2+v2, str)
    for v1, v2 in vowels2.items():
        str = re.sub(v1, v2, str)
    return str