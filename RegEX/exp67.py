import re

def detect_keyword(sentence, keyword):
    pattern = rf"\b{re.escape(keyword)}\b"
    if re.search(pattern, sentence, re.IGNORECASE):
        print(f'Keyword "{keyword}" found in sentence.')
    else:
        print(f'Keyword "{keyword}" NOT found in sentence.')
sentence=input("Enter sentence: ")
keyword=input("Enter keyword: ")
detect_keyword(sentence, keyword)