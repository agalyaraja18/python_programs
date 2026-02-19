sentence = "this is a sentence involving AI and ML technologies"
acronyms = {"AI", "ML", "USA", "IBM"}
title_cased_sentence = " ".join([word.upper() if word.upper() in acronyms else word.title() for word in sentence.split(" ")])
print(title_cased_sentence)
